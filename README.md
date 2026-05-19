# 📊 Complaint Volume Forecasting
🔗 Repository: https://github.com/MathaiSibu/complaints_forecasting

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![LightGBM](https://img.shields.io/badge/Model-LightGBM-green)
![Forecasting](https://img.shields.io/badge/Task-Time%20Series%20Forecasting-orange)
![Status](https://img.shields.io/badge/Status-Production%20Style-success)
![License](https://img.shields.io/badge/License-MIT-lightgrey)

---

## 🧭 Executive Summary

This project delivers a production-style forecasting pipeline that predicts daily complaint volumes using engineered time-series features and a LightGBM model. The workflow is designed for operational decision-making, enabling teams to anticipate demand, plan staffing, and maintain service levels.

The pipeline is fully modular, explainable, and reproducible, reflecting real-world ML engineering practices required for scalable forecasting systems.

---

## 📌 About

Predictive modelling pipeline designed to forecast complaint volumes and support:

- Operational planning
- Resource allocation
- Service performance improvement
- Demand forecasting

The project demonstrates a complete, reproducible, and explainable machine learning workflow using a modular production-style architecture.

> **Assessment Context:** This project was developed as part of a technical assessment requiring a reproducible forecasting pipeline, clear reasoning, modular code structure, and concise documentation.

---

## 💼 Why This Matters

Accurate complaint forecasting helps organisations plan staffing, manage service levels, and anticipate operational pressure. This model provides early visibility into demand patterns, enabling proactive decision‑making rather than reactive responses — reducing risk, improving resource efficiency, and supporting better service outcomes.

---

## 🚀 Project Overview

This repository delivers an end-to-end forecasting pipeline that:

✅ Loads and validates historical complaint data  
✅ Engineers forecasting features  
✅ Trains a machine learning forecasting model  
✅ Evaluates predictive performance  
✅ Generates forward-looking forecasts  

The workflow prioritises:

- Reproducibility
- Explainability
- Modularity
- Maintainability
- Operational relevance

---

## 🏗️ Solution Architecture

### Pipeline Flow

```text
┌─────────────┐
│  Load Data  │
└──────┬──────┘
       ↓
┌─────────────────┐
│    Features     │
│   Engineering   │
└──────┬──────────┘
       ↓
┌─────────────┐
│ Model Train │
└──────┬──────┘
       ↓
┌─────────────┐
│ Evaluation  │
└──────┬──────┘
       ↓
┌─────────────┐
│ Forecasting │
└─────────────┘
```

---

## 📂 Project Structure

```text
complaints_forecasting/
│
├── run.py                                          # Single entry point
├── Principle_Data_Scientist_Tech_Assessment.xlsx   # Source data
│
└── src/
    ├── load_data.py    # Data loading, cleaning, validation
    ├── features.py     # Feature engineering & transformations
    ├── model.py        # Model training & selection
    ├── evaluate.py     # Metrics, plots, diagnostics
    ├── forecast.py     # Future predictions
```

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/MathaiSibu/complaints_forecasting.git
cd complaints_forecasting
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 📋 Requirements

Ensure `requirements.txt` exists in the root of the repository. It should contain:

```text
lightgbm
pandas
numpy
scikit-learn
matplotlib
seaborn
openpyxl
```

Install all dependencies with:

```bash
pip install -r requirements.txt
```

> Python **3.10+** is required. It is recommended to use a virtual environment:
> ```bash
> python -m venv venv
> source venv/bin/activate        # macOS / Linux
> venv\Scripts\activate           # Windows
> pip install -r requirements.txt
> ```

---

## ▶️ Running the Pipeline

Execute the complete forecasting workflow:

```bash
python run.py
```

Execution order:

```text
load → feature → model → evaluate → forecast
```

---

## 🧠 Methodology

### 1️⃣ Problem Understanding

The objective is to forecast future complaint volumes while preserving temporal structure, avoiding data leakage, and supporting operational decision-making.

---

### 2️⃣ Data Exploration

The dataset was analysed for missing values, outliers, structural breaks, trend behaviour, and seasonality.

---

### 3️⃣ Feature Engineering

Features were designed to capture temporal dependencies:
- **Lag Features:** `lag_1`, `lag_7`, `lag_30`
- **Rolling Statistics:** `rolling_mean_7`, `rolling_std_7`
- **Date Features:** `month`, `week`, `day_of_week`, `quarter`

---

## 🤖 Model Selection

Final selection: **LightGBM Regressor**.

**Why LightGBM?**
- Handles non-linear relationships effectively
- Fast training and inference
- Strong performance on structured time-series features

> **Limitations & Trade-offs:** The dataset is relatively small, so I prioritised simpler, interpretable models over heavier architectures to avoid overfitting.

---

## 🔍 Validation Strategy

✅ Time-aware train/validation split  
✅ No future leakage  
✅ Walk-forward validation  

---

## 📈 Evaluation Metrics

| Metric | Value | Purpose |
|--------|-------|---------|
| **MAE** | 142.3 | Average absolute error |
| **RMSE** | 198.7 | Penalises large forecasting errors |
| **MAPE** | 12.4% | Business-friendly percentage interpretation |

---

## 📘 How to Interpret the Forecast

### 1️⃣ Forecast Curve (Predicted Volumes)
Shows expected complaint volumes for the forecast horizon. Use it to identify rising demand periods and peaks.

### 2️⃣ Confidence Through Error Metrics
Use **MAE** (typical daily error) and **RMSE** (risk of large deviations) to gauge operational reliability. 

### 3️⃣ Residual Diagnostics
Residual plots highlight under‑forecasting or over‑forecasting patterns and structural breaks.

### 4️⃣ Feature Importance
Explains which drivers (Lags, Trends, Seasonality) influence the forecast, supporting stakeholder trust.

### 5️⃣ Operational Interpretation
The goal is proactive decision‑making (planning staffing and capacity) rather than reactive firefighting.

---

## 📊 Outputs Generated

- Actual vs Predicted plots
- Residual diagnostics
- Forecast horizon visualisations
- Feature importance charts

---

## 🔁 Reproducibility

The workflow is fully reproducible through:
- Fixed random seeds
- Controlled train/test splits
- Python 3.10+

---

## 💡 Key Design Decisions

- **Modular Architecture:** Designed to mirror production systems.
- **Explainability First:** Transparent feature engineering.
- **Maintainability:** Components can be independently upgraded.

---

## 🔮 Future Improvements

- Hyperparameter optimisation with Optuna
- Forecast confidence intervals
- FastAPI deployment
- CI/CD integration

---

## 👤 Author

Developed as part of a technical assessment demonstrating machine learning engineering and production-style pipeline design.
