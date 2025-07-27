# Data-Analytics-for-Insurance-Cost-Data-Set


# 💼 Insurance Cost Prediction App

This project leverages **machine learning** to estimate individual **medical insurance costs** based on demographic and health-related factors. It uses **Ridge Regression** to improve prediction stability and is deployed with a **Streamlit** web app for user interaction.

---

## 📘 Project Summary

- **Domain:** Health / Insurance
- **Goal:** Predict insurance charges for individuals based on personal attributes.
- **Approach:** Regularized regression (Ridge) with polynomial feature expansion to handle non-linear relationships.
- **Deployment:** Interactive web app built with **Streamlit** and hosted on **Streamlit Cloud**.

---

## 🧠 Objective

To build and deploy a **robust regression model** that accurately estimates medical insurance charges, with the following steps:

1. Clean and preprocess the data.
2. Apply scaling and polynomial feature engineering.
3. Fit a Ridge Regression model to reduce overfitting.
4. Build a simple UI for real-time predictions.

---

## 📊 Dataset Description

- **Dataset Name:** `insurance.csv`
- **Source:** [Kaggle: Medical Cost Personal Dataset](https://www.kaggle.com/datasets/mirichoi0218/insurance)
- **Target Variable:** `charges` (insurance cost)
- **Features Used:**
  | Column         | Description                                      |
  |----------------|--------------------------------------------------|
  | `age`          | Age of the insured individual                    |
  | `bmi`          | Body Mass Index (weight/height²)                 |
  | `children`     | Number of dependent children                     |
  | `smoker`       | Smoking status (`yes` or `no`)                   |
  | `region`       | Residential area (not used in model)             |
  | `charges`      | Target variable — insurance cost in USD          |

---

## 🧹 Data Cleaning Steps

- Renamed columns for clarity.
- Converted `smoker` column to binary (1 = yes, 0 = no).
- Removed rows with missing values.
- Selected numeric and binary columns for modeling (`age`, `bmi`, `children`, `smoker`).

---

## 🧪 Model Pipeline

- **Scaling**: `StandardScaler` normalizes input features.
- **Feature Engineering**: `PolynomialFeatures(degree=2)` expands features to capture non-linear relationships.
- **Model**: `Ridge Regression` (with `alpha=1.0`) balances bias-variance tradeoff.
- **Framework**: `scikit-learn`

---

## 🖥 App Functionality (Streamlit)

Users input:

- Age
- BMI
- Number of Children
- Smoking Status

Then click **"Predict Insurance Charges"** to get an estimate.

> The model automatically preprocesses user input before prediction to ensure accuracy.

---

## 🗂 Project Structure

```
📦 Insurance Cost Prediction App
├── insurance.csv          # Cleaned dataset
├── app.py                 # Streamlit application script
├── requirements.txt       # Python dependencies
└── README.md              # Project documentation
```

---

## 💻 How to Run Locally

1. Clone the repository:

```bash
git clone https://github.com/your-username/insurance-cost-prediction.git
cd insurance-cost-prediction
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run the app:

```bash
streamlit run app.py
```

---

## 🌐 Deployment on Streamlit Cloud

- Ensure your **`insurance.csv`** file is in the **same folder** as `app.py`.
- If running into file path errors, the script handles both local and cloud deployments using:

```python
import os
csv_path = os.path.join(os.path.dirname(__file__), "insurance.csv")
```

- Push to GitHub and connect your repo to [Streamlit Cloud](https://streamlit.io/cloud).

---

## 📦 requirements.txt

```txt
streamlit==1.35.0
pandas==2.2.2
numpy==1.26.4
scikit-learn==1.4.2
```

---

## ✅ Status

- [x] Data cleaning complete  
- [x] Ridge model trained and tuned  
- [x] Streamlit UI built  
- [x] Streamlit Cloud deployment working

---

## 👤 Author

**Christopher Christain G.**  
*Machine Learning & Data Science Enthusiast*  
📍 Nigeria

---

## 💬 Feedback & Contributions

If you have suggestions, feel free to open an issue or submit a pull request. Contributions are welcome!
