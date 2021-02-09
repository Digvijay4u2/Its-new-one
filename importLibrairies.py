# -*- coding: utf-8 -*-
"""
Created on Wed Feb  3 20:25:48 2021

@author: digvijay
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


dataset=pd.read_csv('Data.csv')
print(dataset)

X=dataset.iloc[:,:-1].values
Y=dataset.iloc[:,3].values
#print(X)

# take care of missing data
from sklearn.impute import SimpleImputer
imputer=SimpleImputer(missing_values=np.nan,strategy='mean')
imputer=imputer.fit(X[:,1:3])
X[:,1:3]=imputer.transform(X[:,1:3])
#print(X)




