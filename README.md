# 🍷 Wine Quality Prediction System using Machine Learning

![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-ML-orange?logo=scikitlearn)
![Streamlit](https://img.shields.io/badge/Streamlit-Web%20App-red?logo=streamlit)
![License](https://img.shields.io/badge/License-MIT-green)

A complete end-to-end Machine Learning project that predicts wine quality based on its chemical properties. The project includes data preprocessing, exploratory data analysis, feature engineering, model training, hyperparameter tuning, model explainability, and a Streamlit web application.

---

## 📌 Table of Contents

- Project Overview
- Business Problem
- Dataset
- Technologies Used
- Project Workflow
- Folder Structure
- Machine Learning Pipeline
- Model Performance
- Streamlit Application
- Installation
- How to Run
- Future Improvements
- Author

---

# 📖 Project Overview

Wine quality is traditionally evaluated by expert wine tasters. This process is expensive, subjective, and time-consuming.

This project uses Machine Learning to predict wine quality based on physicochemical properties such as acidity, alcohol content, pH, sulphates, and density.

---

# 🎯 Business Problem

Develop a machine learning model capable of predicting the quality of wine from laboratory measurements, helping wineries perform faster and more consistent quality assessment.

---

# 📊 Dataset

**Source:**

https://www.kaggle.com/datasets/yasserh/wine-quality-dataset

The dataset contains chemical characteristics of wine and their corresponding quality ratings.

### Features

- Fixed Acidity
- Volatile Acidity
- Citric Acid
- Residual Sugar
- Chlorides
- Free Sulfur Dioxide
- Total Sulfur Dioxide
- Density
- pH
- Sulphates
- Alcohol

### Target

Quality (Wine Rating)

---

# 🛠 Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Plotly
- Scikit-Learn
- Streamlit
- Joblib
- Jupyter Notebook

---

# 📂 Project Structure

```text
Wine Quality Prediction/
│
├── app.py
├── requirements.txt
├── README.md
├── LICENSE
│
├── artifacts
│   ├── best_model.pkl
│   ├── scaler.pkl
│   └── final_features.pkl
│
├── data
│   ├── raw
│   └── processed
│
├── notebooks
│   ├── 01_Data_Understanding.ipynb
│   ├── 02_Exploratory_Data_Analysis.ipynb
│   ├── 03_Data_Preprocessing.ipynb
│   ├── 04_Feature_Engineering.ipynb
│   ├── 05_Model_Training.ipynb
│   ├── 06_Model_Evaluation.ipynb
│   ├── 07_Hyperparameter_Tuning.ipynb
│   ├── 08_Model_Explainability.ipynb
│   ├── 09_Test_Modules.ipynb
│   └── 10_Test_Prediction.ipynb
│
├── reports
│
└── src
    ├── data_preprocessing.py
    └── prediction.py
```

---

# ⚙ Machine Learning Pipeline

- Data Collection
- Data Cleaning
- Exploratory Data Analysis
- Feature Engineering
- Feature Scaling
- Model Training
- Model Evaluation
- Hyperparameter Tuning
- Model Explainability
- Model Serialization
- Prediction Pipeline
- Streamlit Deployment

---

# 🤖 Machine Learning Models

The following classifiers were trained and compared:

- Random Forest Classifier
- Support Vector Classifier (SVC)
- Stochastic Gradient Descent (SGD) Classifier

The best-performing model after hyperparameter tuning was selected for deployment.

---

# 📈 Model Performance

| Model | Accuracy |
|--------|---------:|
| Support Vector Classifier | 60.29% |
| Random Forest | 58.82% |
| SGD Classifier | 58.33% |

---

# 🖥 Streamlit Web Application

The web application allows users to:

- Enter wine chemical properties
- Predict wine quality
- Display confidence score
- View input summary
- Visualize chemical properties
- Download prediction report

---

# 🚀 Installation

Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/Wine-Quality-Prediction.git
```

Go inside the folder

```bash
cd Wine-Quality-Prediction
```

Create virtual environment

```bash
python -m venv .venv
```

Activate virtual environment

Windows

```bash
.venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run Streamlit

```bash
streamlit run app.py
```

---

# 📌 Future Improvements

- XGBoost
- LightGBM
- CatBoost
- SHAP Explainability
- Docker
- FastAPI
- MLflow
- CI/CD
- Cloud Deployment
- REST API

---

# 👩‍💻 Author

**Diya Sarkar**

B.Tech Information Technology

Machine Learning | Data Science | Full Stack Development

---

# ⭐ If you found this project useful, please consider giving it a star.