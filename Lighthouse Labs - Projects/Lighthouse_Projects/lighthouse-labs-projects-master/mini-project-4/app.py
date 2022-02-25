import numpy as np
import pandas as pd
from flask import Flask, render_template, request
import pickle
from transformers import *


app = Flask(__name__)
model = pickle.load(open("../output/logregmodel_balanced.sav", "rb"))

columns = ['Gender', 'Married', 'Dependents', 'Education', 'Self_Employed',
            'ApplicantIncome', 'CoapplicantIncome', 'LoanAmount', 'Loan_Amount_Term',
            'Credit_History', 'Property_Area']

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    gender = request.form.get('Gender')
    married = request.form.get('Marriage')
    dependents = request.form.get('Dependents')
    education = request.form.get('Education')
    self_employed = request.form.get('Employed')
    credit_history = request.form.get('Credit')
    property = request.form.get('Property')

    applicant_income = request.form.get('applicant_income', type=float)
    coapp_income = request.form.get('coapp_income', type=float)
    loan_amount = request.form.get('loan_amount', type=float)
    loan_term = request.form.get('loan_term', type=float)

    data = [gender, married, dependents, education, self_employed, applicant_income,
            coapp_income, loan_amount, loan_term, credit_history, property]
    
    df = pd.DataFrame([data], columns=columns)

    prediction = model.predict(df)

    if prediction == float(1):
        output = 'approved!'
    elif prediction == float(0):
        output = 'not approved.'

    return render_template("index.html", prediction_text= 'Your loan is most likely {}'.format(output))

if __name__ == '__main__':
    app.debug = True
    app.run()