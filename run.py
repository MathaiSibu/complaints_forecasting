# -*- coding: utf-8 -*-
"""
Created on Tue May 19 07:39:12 2026

@author: kmsib
"""
# -*- coding: utf-8 -*-
"""
Created on Tue May 19 07:39:12 2026

@author: kmsib
"""

from src.load_data import load_data
from src.features import create_features
from src.model import build_model
from src.evaluate import evaluate_model
from src.forecast import recursive_forecast

import pandas as pd
import matplotlib.pyplot as plt

def main():
    df = load_data('Principle_Data_Scientist_Tech_Assessment.xlsx')
    df_feat = create_features(df)

    X = df_feat.drop(columns=['complaints'])
    y = df_feat['complaints']

    split = int(len(df_feat) * 0.8)
    X_train, X_test = X.iloc[:split], X.iloc[split:]
    y_train, y_test = y.iloc[:split], y.iloc[split:]

    model = build_model()
    model.fit(X_train, y_train)

    # --- Feature Importance ---
    importances = model.feature_importances_
    feature_names = X_train.columns

    fi_df = pd.DataFrame({
        'feature': feature_names,
        'importance': importances
    }).sort_values(by='importance', ascending=False)

    print("\nTop Features Driving the Forecast:")
    print(fi_df)

    plt.figure(figsize=(10, 6))
    plt.barh(fi_df['feature'], fi_df['importance'])
    plt.gca().invert_yaxis()
    plt.title("LightGBM Feature Importance")
    plt.xlabel("Importance Score")
    plt.tight_layout()
    plt.show()

    # --- Evaluation ---
    mae, rmse, preds = evaluate_model(model, X_test, y_test)
    print(f"MAE: {mae:.2f}, RMSE: {rmse:.2f}")

    # --- Actual vs Predicted Plot ---
    plt.figure(figsize=(12, 6))
    plt.plot(y_test.index, y_test, label='Actual', linewidth=2)
    plt.plot(y_test.index, preds, label='Predicted', linewidth=2)
    plt.title("Actual vs Predicted Complaints")
    plt.xlabel("Date")
    plt.ylabel("Complaints")
    plt.legend()
    plt.tight_layout()
    plt.show()

    # --- Forecast ---
    forecast_df = recursive_forecast(model, df_feat, horizon=90)
    print(forecast_df.head())

    # --- Forecast Plot ---
    plt.figure(figsize=(12, 6))
    plt.plot(df_feat.index[-60:], df_feat['complaints'].iloc[-60:], 
             label='Actual (last 60 days)', linewidth=2)
    plt.plot(forecast_df['date'], forecast_df['forecast'], 
             label='Forecast (next 90 days)', linewidth=2)
    plt.title("90-Day Forecast of Complaints")
    plt.xlabel("Date")
    plt.ylabel("Complaints")
    plt.legend()
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
