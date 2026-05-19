# -*- coding: utf-8 -*-
"""
Created on Tue May 19 06:55:08 2026

@author: kmsib
"""

# src/load_data.py

import pandas as pd

def load_data(path):
    df = pd.read_excel(path, sheet_name='daily records')
    df['date'] = pd.to_datetime(df['date'])

    # Drop meaningless ID column
    df = df.drop(columns=['row_id'])

    df = df.dropna(subset=['complaints']).copy()

    numeric_cols = ['staffing_level_fte', 'media_mentions', 'channel_mix_index']
    for col in numeric_cols:
        df[col] = df[col].fillna(df[col].median())

    df = df.set_index('date').sort_index()
    return df
