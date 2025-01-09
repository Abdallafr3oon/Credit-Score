# Credit Score Prediction

This project focuses on developing a robust machine learning model to predict credit scores based on customer attributes such as income, payment behavior, and credit utilization. The goal is to enable financial institutions to assess creditworthiness efficiently and provide personalized financial solutions.

## Table of Contents
1. [Dataset Overview](#dataset-overview)
2. [Data Cleaning Process](#data-cleaning-process)
3. [Handling Imbalanced Data](#handling-imbalanced-data)
4. [Feature Selection](#feature-selection)
5. [Data Visualization](#data-visualization)
6. [Model Training and Evaluation](#model-training-and-evaluation)
7. [Results](#results)
8. [Flask Web Application](#flask-web-application)
9. [Installation and Usage](#installation-and-usage)
10. [License](#license)

## Dataset Overview

The dataset contains 100,000 entries and 28 columns, including a mix of numerical and categorical variables:

### Numerical Columns:
- Monthly_Inhand_Salary
- Num_Bank_Accounts
- Num_Credit_Card
- Interest_Rate
- Delay_from_due_date
- Num_Credit_Inquiries
- Credit_Utilization_Ratio
- Total_EMI_per_month
- ... (other numerical features)

### Categorical Columns:
- ID
- Customer_ID
- Name
- Age
- SSN
- Occupation
- Type_of_Loan
- Credit_Mix
- Payment_Behaviour
- ... (other categorical features)

### Target Variable:
- **Credit_Score** (classified into three categories):
  - **Good**: 17,828 instances
  - **Poor**: 28,998 instances
  - **Standard**: 53,174 instances

## Data Cleaning Process

To prepare the dataset for analysis, the following steps were taken:

### Cleaning Numerical Columns:
- Removed invalid characters (e.g., underscores, commas).
- Converted columns to appropriate numerical types (float or int).

### Cleaning Categorical Columns:
- Standardized categories (e.g., replaced placeholders with "Unknown").
- Removed or mapped invalid entries (e.g., special symbols).

### Handling Missing Values:
- Numerical columns: Imputed missing values with the median or mean.
- Categorical columns: Filled missing values with the mode or "Unknown".

### Ensuring Consistent Data Types:
- Numerical columns were converted to float or int.
- Categorical columns were encoded as category.

## Handling Imbalanced Data

The dataset exhibits an imbalanced distribution of credit scores, which could lead to biased predictions. To address this, the following strategies were employed:

- **Oversampling Minority Classes**: Used SMOTE (Synthetic Minority Oversampling Technique) to generate synthetic samples for minority classes.
- **Handling Outliers**: Removed outliers based on a range defined by the mean ± 4 times the standard deviation.

## Feature Selection

Irrelevant or redundant columns were removed to improve model efficiency and reduce overfitting. The following columns were removed:

- Name, ID, Customer_ID: Unique identifiers that do not contribute to credit score prediction.
- SSN: Sensitive data with no predictive value.
- Month: Time-related variable with little influence on credit scores.
- Type_of_Loan: Significant missing values and less relevance to the objective.

## Data Visualization

- **Correlation Heatmap**: Revealed strong positive correlations between "Annual_Income" and "Monthly_Inhand_Salary".
- **Credit Score Distribution**: Highlighted the imbalance in the dataset, with most customers having a "Standard" credit score.
- **Age vs. Credit Score**: Showed that individuals with "Good" credit scores span a wide age range.
- **Monthly Balance vs. Credit Score**: Minimal variability across credit score categories.
- **Outstanding Debt vs. Credit Score**: Wider debt distribution for individuals with "Poor" credit scores.

## Model Training and Evaluation

### Models Used:
- **Random Forest Classifier**:
  - Accuracy: 86%
  - Precision, Recall, F1-score:
    - Good: 0.87, 0.89, 0.88
    - Standard: 0.86, 0.76, 0.81
    - Poor: 0.86, 0.95, 0.90

- **XGBoost Classifier**:
  - Accuracy: 81%
  - Precision, Recall, F1-score:
    - Good: 0.84, 0.81, 0.82
    - Standard: 0.78, 0.72, 0.75
    - Poor: 0.91, 0.91, 0.86

- **Deep Learning Model**:
  - Accuracy: 79%
  - Precision, Recall, F1-score:
    - Good: 0.80, 0.84, 0.82
    - Standard: 0.78, 0.64, 0.70
    - Poor: 0.80, 0.91, 0.85

## Results

- **Random Forest** performed the best, achieving the highest accuracy and strong performance across all classes.
- **XGBoost** and the **Deep Learning Model** also performed well but struggled with the "Standard" credit score class.
- The models excelled in predicting "Poor" credit scores, which is critical for risk assessment.

## Flask Web Application

A **Flask** web application was developed to allow users to input their financial details and receive a credit score prediction. The app includes:

- A user-friendly form for inputting financial data.
- A prediction route that processes inputs and displays the result.
- Pre-trained models (XGBoost or Random Forest) for real-time predictions.

## Installation and Usage

### Clone the Repository:
```bash
git clone https://github.com/your-username/credit-score-prediction.git
cd credit-score-prediction

