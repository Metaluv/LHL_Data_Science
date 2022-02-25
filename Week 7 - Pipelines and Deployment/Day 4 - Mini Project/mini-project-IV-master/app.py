# import Flask and jsonify
from flask import Flask, jsonify, request
# import Resource, Api and reqparser
from flask_restful import Resource, Api, reqparse
import pandas as pd
import numpy
import pickle
from sklearn.pipeline import Pipeline
from sklearn.tree import DecisionTreeClassifier
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.svm import SVC

app = Flask(__name__)
api = Api(app)

model = pickle.load(open(
    "../../../../../../Downloads/lighthouse-data-notes-master (1)/lighthouse-data-notes-master/Week_7/Day_4/mini-project-IV-master/model_p", "rb"))


class Scoring(Resource):
    def post(self):
        json_data = request.get_json()
        df = pd.read_json(json_data)
        # getting predictions from our model.
        # it is much simpler because we used pipelines during development
        res = model.predict(df)
        # we cannot send numpy array as a result
        return res.tolist() 

# assign endpoint
api.add_resource(Scoring, '/scoring')


if __name__ == '__main__':
    app.run(debug=True, port=5555)