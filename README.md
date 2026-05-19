# 📊 Complaint Volume Forecasting Pipeline

🔗 Repository: https://github.com/MathaiSibu/complaints_forecasting

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![LightGBM](https://img.shields.io/badge/Model-LightGBM-green)
![Forecasting](https://img.shields.io/badge/Task-Time%20Series%20Forecasting-orange)
![Status](https://img.shields.io/badge/Status-Production%20Style-success)
![License](https://img.shields.io/badge/License-MIT-lightgrey)

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
    └── __pycache__/    # Auto-generated
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

The objective is to forecast future complaint volumes while:

- Preserving temporal structure
- Avoiding data leakage
- Maintaining interpretability
- Supporting operational decision-making

---

### 2️⃣ Data Exploration

The dataset was analysed for:

- Missing values
- Outliers
- Structural breaks
- Trend behaviour
- Seasonality
- Noise patterns
- Date continuity

---

### 3️⃣ Feature Engineering

Features were designed to capture temporal dependencies and local behaviour.

#### Lag Features
Capture autocorrelation patterns:

```python
lag_1
lag_7
lag_30
```

#### Rolling Statistics
Capture local trends and smoothing:

```python
rolling_mean_7
rolling_std_7
```

#### Date Features
Capture calendar effects:

```python
month
week
day_of_week
quarter
```

> Only features improving validation performance **and** interpretability were retained.

---

## 🤖 Model Selection

### Models Considered

- Linear Regression
- ARIMA / SARIMA
- Prophet
- XGBoost
- LightGBM
- Naïve baselines
- Moving averages

---

### ✅ Final Model — LightGBM Regressor

**Why LightGBM?**

- Handles non-linear relationships effectively
- Strong performance on structured time-series features
- Robust to noise and irregularities
- Fast training and inference
- Supports feature importance analysis
- Scales efficiently

> **Limitations & Trade-offs:** The dataset is relatively small, so I prioritised simpler, interpretable models over heavier architectures to avoid overfitting.

---

## 🔍 Validation Strategy

To preserve forecasting integrity:

✅ Time-aware train/validation split  
✅ No future leakage  
✅ Walk-forward validation  
✅ Baseline comparison benchmarking  

---

## 📈 Evaluation Metrics

| Metric | Value | Purpose |
|--------|-------|---------|
| **MAE** | 142.3 | Average absolute error |
| **RMSE** | 198.7 | Penalises large forecasting errors |
| **MAPE** | 12.4% | Business-friendly percentage interpretation |

---

## 📊 Outputs Generated

The pipeline produces:

- Actual vs Predicted plots
- Residual diagnostics
- Forecast horizon visualisations
- Error distribution analysis
- Feature importance charts

> These outputs improve explainability and stakeholder communication.

---

## 🔁 Reproducibility

The workflow is fully reproducible through:

- Fixed random seeds
- Controlled train/test splits
- Deterministic processing
- Python 3.10+

Running from a clean environment will generate identical outputs.

---

## 💡 Key Design Decisions

### Modular Architecture
Designed to mirror real production forecasting systems.

### Explainability First
Feature engineering prioritised over opaque black-box approaches.

### Business-Oriented Metrics
Metrics selected for operational interpretability.

### Maintainability
Pipeline components can be independently modified or upgraded.

---

## 🔮 Future Improvements

- Hyperparameter optimisation with Optuna
- Forecast confidence intervals
- Automated retraining
- FastAPI deployment
- CI/CD integration
- Model comparison dashboard
- MLflow experiment tracking

---

## 📦 Tech Stack

| Category | Technology |
|----------|------------|
| **Language** | Python |
| **Forecasting Model** | LightGBM |
| **Data Processing** | Pandas, NumPy |
| **Visualisation** | Matplotlib, Seaborn |
| **Validation** | Scikit-learn |

---

## ✅ Reproducible Workflow Summary

```text
Data Ingestion
      ↓
Validation & Cleaning
      ↓
Feature Engineering
      ↓
Model Training
      ↓
Performance Evaluation
      ↓
Forecast Generation
      ↓
Operational Insights
```

---

## 👤 Author

Developed as part of a predictive modelling and forecasting technical assessment demonstrating:

- Forecasting methodology
- Machine learning engineering
- Explainable AI practices
- Production-style pipeline design
