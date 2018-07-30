# -*- coding: utf-8 -*-
"""
Created on Mon Jul 30 15:47:45 2018

@author: Sales India
"""

import pandas as pd

train = pd.read_csv("Downloads/all/train.csv")

xtrain = train[['Pclass', 'Sex', 'Age','Parch']]
ytrain = train[['Survived']]

test = pd.read_csv("Downloads/all/test.csv")
xtest = test[['Pclass', 'Sex', 'Age','Parch']] 


from sklearn.preprocessing import LabelEncoder
lb = LabelEncoder()
xtrain[['Sex']] = lb.fit_transform(xtrain[['Sex']])
xtest[['Sex']] = lb.fit_transform(xtest[['Sex']])

from sklearn.preprocessing import Imputer
imputer = Imputer(missing_values="NaN", strategy="mean")
xtrain = imputer.fit_transform(xtrain)
xtest = imputer.fit_transform(xtest)

from sklearn.linear_model import LogisticRegression
lr = LogisticRegression()
lr.fit(xtrain, ytrain)

ypred = lr.predict(xtest)

ypred = pd.DataFrame(ypred[[0]]).to_csv('pred.csv')
