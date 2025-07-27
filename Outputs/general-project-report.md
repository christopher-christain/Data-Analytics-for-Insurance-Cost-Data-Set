# 📘 General Project Report

## 🧠 Objective
To analyze healthcare insurance cost data and build a predictive model to estimate insurance charges based on customer features such as age, smoking status, BMI, and region.

## 🔬 Exploratory Data Analysis
- Used **regression plots** and **boxplots** to visualize the relationship between:
  - `BMI` and `Charges`
  - `Smoker` status and `Charges`
- Observations:
  - **Smokers** are charged significantly higher.
  - BMI also shows a mild positive correlation with charges.

## 🛠️ Modeling Approach
- Used **Linear Regression** and **Ridge Regression** models.
- Built a **pipeline** with:
  - `StandardScaler` → `PolynomialFeatures` → `LinearRegression`
- Improved performance using **Ridge Regression** with polynomial features (degree=2).

## 📈 Model Performance
- **Linear Regression R² (training set)**: Printed directly.
- **Ridge Regression R² (test set)**: Achieved good generalization.
- **Ridge + Polynomial Features R²**: Improved model accuracy further, reducing underfitting.
