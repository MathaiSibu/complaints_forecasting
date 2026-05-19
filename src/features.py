# -*- coding: utf-8 -*-
"""
Created on Tue May 19 07:06:46 2026

@author: kmsib
"""

import pandas as pd

def create_features(df):
    df = df.copy()

    # Lag features
    for lag in [1, 7, 14, 28]:
        df[f'lag_{lag}'] = df['complaints'].shift(lag)

    # Rolling windows
    df['roll_mean_7'] = df['complaints'].rolling(7).mean()
    df['roll_std_7'] = df['complaints'].rolling(7).std()
    df['roll_mean_30'] = df['complaints'].rolling(30).mean()
    df['roll_std_30'] = df['complaints'].rolling(30).std()

    # Calendar features
    df['day_of_week'] = df.index.dayofweek
    df['month'] = df.index.month
    df['is_month_start'] = df.index.is_month_start.astype(int)
    df['is_month_end'] = df.index.is_month_end.astype(int)

    df = df.dropna()
    return df
