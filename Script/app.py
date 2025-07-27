import streamlit as st
import pandas as pd
import numpy as np
import os
from sklearn.preprocessing import StandardScaler, PolynomialFeatures
from sklearn.linear_model import Ridge

# Initialize model components
scaler = StandardScaler()
poly = PolynomialFeatures(degree=2)
model = Ridge(alpha=1.0)

@st.cache_data
def train_model():
    # Attempt to locate insurance.csv in common locations
    possible_paths = [
        "insurance.csv",
        "./insurance.csv",
        "../insurance.csv",
        os.path.join(os.path.dirname(__file__), "insurance.csv"),
        os.path.join(os.path.dirname(__file__), "../insurance.csv")
    ]

    for path in possible_paths:
        if os.path.exists(path):
            data_path = path
            break
    else:
        st.error("❌ 'insurance.csv' not found in any expected locations.")
        st.stop()

    # Load and clean data
    data = pd.read_csv(data_path)
    data.columns = ["age", "gender", "bmi", "no_of_children", "smoker", "region", "charges"]
    data["smoker"] = data["smoker"].replace({"yes": 1, "no": 0})
    data.dropna(inplace=True)

    # Features & Target
    X = data[["age", "bmi", "no_of_children", "smoker"]].astype(float)
    y = data["charges"]

    # Train the model
    X_scaled = scaler.fit_transform(X)
    X_poly = poly.fit_transform(X_scaled)
    model.fit(X_poly, y)

train_model()

# ───────────── Streamlit UI ─────────────
st.title("🩺 Insurance Charges Prediction App")

st.markdown("Enter the individual's information below to predict their estimated insurance charges:")

# User inputs
age = st.number_input("Age", min_value=1, max_value=120, value=30)
bmi = st.number_input("BMI", min_value=10.0, max_value=60.0, value=25.0)
children = st.number_input("Number of Children", min_value=0, max_value=10, value=0)
smoker = st.selectbox("Do they smoke?", ["no", "yes"])
smoker_val = 1 if smoker == "yes" else 0

# Prediction trigger
if st.button("Predict Insurance Charges"):
    input_data = np.array([[age, bmi, children, smoker_val]])
    input_scaled = scaler.transform(input_data)
    input_poly = poly.transform(input_scaled)
    prediction = model.predict(input_poly)[0]

    st.success(f"💰 Estimated Insurance Charges: ${prediction:,.2f}")
