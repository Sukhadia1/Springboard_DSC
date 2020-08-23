import pandas as pd

from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import GridSearchCV

def logistic(df):
    X = pd.get_dummies(df.drop('status_group', axis=1))
    y = df.status_group

    lr = LogisticRegression()
    params = {'C': [0.1, 1, 10]}

    clf = GridSearchCV(lr,params, cv=3)

    return clf.fit(X,y)
