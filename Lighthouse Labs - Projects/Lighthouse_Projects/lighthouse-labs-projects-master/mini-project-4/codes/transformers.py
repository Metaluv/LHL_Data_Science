import pandas as pd
import numpy as np

class DataframeFunctionTransformer():
    def __init__(self, func):
        self.func = func
        
    def transform(self, input_df, **transform_params):
        return self.func(input_df)
    
    def fit(self, X, y=None, **fit_params):
        return self

class SelectColumnsTransformer():
    def __init__(self, columns=None):
        self.columns = columns

    def transform(self, X, **transform_params):
        cpy_df = X[self.columns].copy()
        return cpy_df

    def fit(self, X, y=None, **fit_params):
        return self

def get_total_income(input_df):
    try: 
        input_df['total_income'] = input_df['ApplicantIncome'] + input_df['CoapplicantIncome']
        input_df.drop(['ApplicantIncome', 'CoapplicantIncome'], axis=1, inplace=True)
    except: 
        pass
    return input_df

def get_log_transform(input_df):
    input_df['total_income'] = np.log10(input_df['total_income'])
    input_df['LoanAmount'] = np.log10(input_df['LoanAmount'])
    return input_df