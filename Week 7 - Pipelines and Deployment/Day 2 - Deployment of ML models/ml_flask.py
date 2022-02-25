import pandas as pd
from sklearn.datasets import load_wine

from sklearn.model_selection import GridSearchCV
from sklearn.pipeline import Pipeline, FeatureUnion

from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.feature_selection import SelectKBest

from sklearn.ensemble import RandomForestClassifier

import pickle


data = load_wine()
df = pd.DataFrame(data['data'])
df.columns = data['feature_names']
y = data['target']
df.head()


# own class that can be inserted to pipeline as any other sklearn object.
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


# features we want to keep for PCA
feats = ['alcohol','malic_acid','ash','alcalinity_of_ash','magnesium',
         'total_phenols','flavanoids','nonflavanoid_phenols']
# creating class object with indexes we want to keep.
raw_feats = RawFeats(feats)



sc = StandardScaler()
pca = PCA(n_components=2)


selection = SelectKBest(k=4)

rf = RandomForestClassifier()


PCA_pipeline = Pipeline([
    ("rawFeats", raw_feats),
    ("scaler", sc),
    ("pca", pca)
])

kbest_pipeline = Pipeline([("kBest", selection)])


all_features = FeatureUnion([
    ("pcaPipeline", PCA_pipeline), 
    ("kBestPipeline", kbest_pipeline)
])

main_pipeline = Pipeline([
    ("features", all_features),
    ("rf", rf)
])


# set up our parameters grid
param_grid = {"features__pcaPipeline__pca__n_components": [1, 2, 3],
                  "features__kBestPipeline__kBest__k": [1, 2, 3],
                  "rf__n_estimators":[2, 5, 10],
                  "rf__max_depth":[2, 4, 6]
             }

# create a Grid Search object
grid_search = GridSearchCV(main_pipeline, param_grid, n_jobs = -1, verbose=10, refit=True)    

# fit the model and tune parameters
grid_search.fit(df, y)


