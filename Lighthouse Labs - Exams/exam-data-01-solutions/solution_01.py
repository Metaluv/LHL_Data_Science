def equal_slices(total_slices, no_recipients, slices_each):
    sol = True if no_recipients * slices_each <= total_slices else False
    remains = total_slices - (no_recipients * slices_each) 
    remains = remains if remains >= 0 else None

    return sol,remains