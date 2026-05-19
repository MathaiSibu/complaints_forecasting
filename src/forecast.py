# -*- coding: utf-8 -*-
"""
Created on Tue May 19 07:37:42 2026

@author: kmsib
"""

import pandas as pd

def recursive_forecast(model, df, horizon=90):
    df = df.copy()
    future_dates = pd.date_range(df.index[-1] + pd.Timedelta(days=1), periods=horizon)

    forecasts = []

    # Get the exact feature columns used during training
    feature_cols = [col for col in df.columns if col != 'complaints']

    for date in future_dates:
        row = {}

        # Lag features
        row['lag_1'] = df['complaints'].iloc[-1]
        row['lag_7'] = df['complaints'].iloc[-7]
        row['lag_14'] = df['complaints'].iloc[-14]
        row['lag_28'] = df['complaints'].iloc[-28]

        # Rolling windows
        row['roll_mean_7'] = df['complaints'].rolling(7).mean().iloc[-1]
        row['roll_std_7'] = df['complaints'].rolling(7).std().iloc[-1]
        row['roll_mean_30'] = df['complaints'].rolling(30).mean().iloc[-1]
        row['roll_std_30'] = df['complaints'].rolling(30).std().iloc[-1]

        # Calendar features
        row['day_of_week'] = date.dayofweek
        row['month'] = date.month
        row['is_month_start'] = int(date.is_month_start)
        row['is_month_end'] = int(date.is_month_end)

        # Exogenous variables (held constant)
        row['staffing_level_fte'] = df['staffing_level_fte'].iloc[-1]
        row['media_mentions'] = df['media_mentions'].iloc[-1]
        row['channel_mix_index'] = df['channel_mix_index'].iloc[-1]
        row['bank_holiday_flag'] = 0

        # Additional features you forgot
        row['backlog_days'] = df['backlog_days'].iloc[-1]
        row['is_weekend'] = int(date.dayofweek >= 5)
        row['centered_7d_mean'] = df['centered_7d_mean'].iloc[-1]

        # Build DataFrame in correct column order
        X = pd.DataFrame([row])[feature_cols]

        y_pred = model.predict(X)[0]
        forecasts.append((date, y_pred))

        # Append prediction to df for next iteration
        df.loc[date, 'complaints'] = y_pred

    return pd.DataFrame(forecasts, columns=['date', 'forecast'])
