from flask import Flask, jsonify, request
from flask_restful import Resource, Api, reqparse
import pandas as pd
import numpy
import pickle

app = Flask(__name__)
api = Api(app)

class RawFeats:
    def __init__(self, feats):
        self.feats = feats

    def fit(self, X, y=None):
        pass


    def transform(self, X, y=None):
        return X[self.feats]

    def fit_transform(self, X, y=None):
        self.fit(X)
        return self.transform(X)
    
model = pickle.load(open(
    '../../../../../Downloads/lighthouse_data_notes-main (1)/lighthouse_data_notes-main/Week_7/Day_2/model.p', 'rb'))

class Scoring(Resource):
    def post(self):
        json_data = request.get_json()
        df = pd.DataFrame(json_data.values(),
                          index=json_data.keys()).transpose()
        res = model.predict_proba(df)
        
        return res.tolist()
    
api.add_resource(Scoring, '/scoring')

if __name__ == '__main__':
    app.run(debug=True,  port=5000)
    
    
        