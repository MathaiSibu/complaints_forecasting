# -*- coding: utf-8 -*-
"""
Created on Tue May 19 07:34:43 2026

@author: kmsib
"""


from lightgbm import LGBMRegressor

def build_model():
    model = LGBMRegressor(
        n_estimators=500,
        learning_rate=0.05,
        max_depth=-1,
        subsample=0.8,
        colsample_bytree=0.8,
        random_state=42
    )
    return model