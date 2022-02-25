from flask import Flask, jsonify
from flask_restful import Resource, Api, reqparse

app = Flask(__name__)
api = Api(app)

class add(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('num1', type=float)
        parser.add_argument('num2', type=float)
        args = parser.parse_args() 
        return args['num1'] + args['num2']

class subtract(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('num1', type=float)
        parser.add_argument('num2', type=float)
        args = parser.parse_args() 
        return args['num1'] - args['num2']
        
class multiply(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('num1', type=float)
        parser.add_argument('num2', type=float)
        args = parser.parse_args() 
        return args['num1'] * args['num2']

class divide(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('num1', type=float)
        parser.add_argument('num2', type=float)
        args = parser.parse_args() 
        return args['num1'] / args['num2']

api.add_resource(add,'/add')
api.add_resource(subtract,'/subtract')
api.add_resource(multiply,'/multiply')
api.add_resource(divide,'/divide')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8088)