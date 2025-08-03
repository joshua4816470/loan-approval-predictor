# Loan Approval Prediction App

A simple machine learning web app built with Python and Streamlit to predict whether a loan application will be approved or rejected based on applicant details.

---

##  Overview

This project uses a classification model (Random Forest Classifier) trained on a loan application dataset. The model predicts loan approval status (`Approved` or `Not Approved`) based on features such as:

- Number of Dependents  
- Education Level  
- Self Employment Status  
- Annual Income  
- Loan Amount  
- Loan Term  
- CIBIL Score  
- Residential, Commercial, Luxury, and Bank Asset Values  

---

##  Project Structure

├── loan_app.py              # Streamlit UI  
├── loan_approval_model.pkl  # Trained Random Forest  
├── data/                    # Raw CSV (optional)  
├── notebook/                # EDA & training workflow  
└── requirements.txt

