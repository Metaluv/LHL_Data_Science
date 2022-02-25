import streamlit as st 
import pandas as pd


property_option = ['Urban', 'Semiurban','Rural']

gender_option=['Male','Female']

education_option = ['Graduate','Not Graduate']

applicant_income_option =[1000,2000,3000,4000,5000,6000,10000,12000,14000]

property = st.selectbox('Option for Property Area', property_option)
gender = st.selectbox('Option for Gender', gender_option)
applicant = st.selectbox('Option for Income', applicant_income_option)
education = st.selectbox('Option for Education Level', education_option)




if st.button('Make my own custom data'):
    data = {
    'Gender': gender,
    'Married': 'Yes',
    'Dependents': '0',
    'Education': education,
    'Self_Employed': 'No',
    'ApplicantIncome': applicant,
    'CoapplicantIncome': 1622,
    'LoanAmount': 150,
    'Loan_Amount_Term': 342.0,
    'Credit_History': 1,
    'Property_Area': property 
    }
    df =pd.DataFrame(data, index=[0])
    st.dataframe(df)
else: 
    st.write('goodbye')