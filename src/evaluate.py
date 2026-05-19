# -*- coding: utf-8 -*-
"""
Created on Tue May 19 07:35:30 2026

@author: kmsib
"""

import numpy as np
from sklearn.metrics import mean_absolute_error, mean_squared_error

def evaluate_model(model, X_test, y_test):
    preds = model.predict(X_test)
    mae = mean_absolute_error(y_test, preds)
    rmse = np.sqrt(mean_squared_error(y_test, preds))
    return mae, rmse, preds