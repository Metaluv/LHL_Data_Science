# import Flask and jsonify
from flask import Flask, jsonify, request
# import Resource, Api and reqparser
from flask_restful import Resource, Api, reqparse

app = Flask(__name__)
api = Api(app)

class calculate(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        
        parser.add_argument('var_1', type = int)
        parser.add_argument('var_2', type = int)
        parser.add_argument('operation', type = str)
        
        var_1 = parser.parse_args().get('var_1')
        var_2 = parser.parse_args().get('var_2')
        operation = parser.parse_args().get('operation')

        if(operation == 'Addition'):
            result = var_1 + var_2
        elif(operation == 'Subtraction'):
            result = var_1 - var_2
        elif(operation == 'Multiplication'):
            result = var_1 * var_2
        elif(operation == 'Division'):
            result = var_1 / var_2
        else:
            result = 'INVALID CHOICE'
        
        return jsonify(result=result)
            
api.add_resource(calculate, '/calculate',)

if __name__ == '__main__':
    app.run(port=5555, debug=True)