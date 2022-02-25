from ortools.constraint_solver import pywrapcp, routing_enums_pb2

distance_matrix = [[0, 884, 719, 2833, 3135, 1070, 1158, 1247, 569, 593],
 [884, 0, 869, 2770, 3072, 230, 782, 1113, 832, 291],
 [719, 869, 0, 3258, 3560, 1058, 733, 497, 1129, 622],
 [2833, 2742, 3258, 0, 373, 2655, 3482, 3627, 2441, 2828],
 [3135, 3044, 3560, 373, 0, 2957, 3784, 3929, 2743, 3130],
 [1074, 230, 1058, 2655, 2957, 0, 971, 1302, 757, 475],
 [1158, 782, 733, 3510, 3812, 971, 0, 470, 1571, 697],
 [1188, 1113, 497, 3627, 3929, 1302, 470, 0, 1598, 915],
 [569, 832, 1129, 2441, 2743, 757, 1572, 1656, 0, 873],
 [593, 291, 622, 2828, 3130, 475, 697, 915, 873, 0]]

def create_data_model():
    """Stores the data for the problem."""
    data = {}
    data['distance_matrix'] = distance_matrix
    data['num_vehicles'] = 1
    data['depot'] = 0
    return data

def print_solution(manager, routing, solution):
    """Prints solution on console."""
    print('Objective: {} meters'.format(solution.ObjectiveValue()))
    index = routing.Start(0)
    plan_output = 'Route for vehicle 0:\n'
    route_distance = 0
    while not routing.IsEnd(index):
        plan_output += ' {} ->'.format(manager.IndexToNode(index))
        previous_index = index
        index = solution.Value(routing.NextVar(index))
        route_distance += routing.GetArcCostForVehicle(previous_index, index, 0)
    plan_output += ' {}\n'.format(manager.IndexToNode(index))
    print(plan_output)
    plan_output += 'Route distance: {}miles\n'.format(route_distance)

def distance_callback(from_index, to_index):
    """Returns the distance between the two nodes."""
    # Convert from routing variable Index to distance matrix NodeIndex.
    from_node = manager.IndexToNode(from_index)
    to_node = manager.IndexToNode(to_index)
    return data['distance_matrix'][from_node][to_node]

data = create_data_model()
manager = pywrapcp.RoutingIndexManager(len(data['distance_matrix']),
                                       data['num_vehicles'], data['depot'])
routing = pywrapcp.RoutingModel(manager)

transit_callback_index = routing.RegisterTransitCallback(distance_callback)

routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)

search_parameters = pywrapcp.DefaultRoutingSearchParameters()
search_parameters.first_solution_strategy = (routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC)

solution = routing.SolveWithParameters(search_parameters)

if solution:
    print_solution(manager, routing, solution)