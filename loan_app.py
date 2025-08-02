import streamlit as st
import numpy as np
import joblib

# Load model
model = joblib.load("loan_approval_model.pkl")

st.title("🏦 Loan Approval Prediction App")

# Input fields
no_of_dependents = st.number_input("Number of Dependents", min_value=0)
education = st.selectbox("Education", ["Graduate", "Not Graduate"])
self_employed = st.selectbox("Self Employed", ["Yes", "No"])
income_annum = st.number_input("Annual Income", min_value=0)
loan_amount = st.number_input("Loan Amount", min_value=0)
loan_term = st.number_input("Loan Term (months)", min_value=0)
cibil_score = st.number_input("CIBIL Score (300–900)", min_value=300, max_value=900)
residential_assets_value = st.number_input("Residential Asset Value", min_value=0)
commercial_assets_value = st.number_input("Commercial Asset Value", min_value=0)
luxury_assets_value = st.number_input("Luxury Asset Value", min_value=0)
bank_asset_value = st.number_input("Bank Asset Value", min_value=0)

# Convert to model-friendly format
education_val = 0 if education == "Graduate" else 1
self_employed_val = 1 if self_employed == "Yes" else 0

input_data = np.array([[no_of_dependents, education_val, self_employed_val,
                        income_annum, loan_amount, loan_term, cibil_score,
                        residential_assets_value, commercial_assets_value,
                        luxury_assets_value, bank_asset_value]])

# Predict
if st.button("Predict Loan Status"):
    prediction = model.predict(input_data)
    status = "✅ Approved" if prediction[0] == 1 else "❌ Rejected"
    st.success(f"Loan Status: {status}")
