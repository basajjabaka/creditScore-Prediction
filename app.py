# 2 - Standard - 35125
# 1 - Good - 18463
# 0 - Poor - 12174

import streamlit as st
import pandas as pd
import numpy as np
import joblib


model = joblib.load("models/best_model_rf.pkl")
encoders = {col: joblib.load(f"models/labelEncoders/encoder_{col}.pkl") for col in ['Month', 'Occupation', 'Credit_Mix', 'Payment_of_Min_Amount',
       'Payment_Behaviour']}

st.title("Credit Score Prediction")
st.write("Enter the applicant's details")

"""# Input fields for applicant's details
applicant_data = {}
for col in catCols:
    applicant_data[col] = st.selectbox(f"Select {col}", options=encoders[col].classes_)

for col in numCols:
    applicant_data[col] = st.number_input(f"Enter {col}", min_value=0.0)

if st.button("Predict"):
    # Preprocess the input data
    input_data = pd.DataFrame([applicant_data])
    for col in catCols:
        input_data[col] = encoders[col].transform(input_data[col])
    input_data = input_data[numCols]

    # Make prediction
    prediction = model.predict(input_data)
    st.write(f"Predicted Credit Score: {prediction[0]}")"""

age = st.number_input("Age", min_value=18, max_value=60, value=25)
annual_income = st.number_input("Annual Income", min_value=0)
monthly_inhand_income = st.number_input("Monthly Inhand Income", min_value=0)
num_bank_accounts = st.number_input("Number of Bank Accounts", min_value=0)
num_credit_card = st.number_input("Number of Credit Card", min_value=0)
interest_rate = st.number_input("Interest Rate", min_value=0.0)
num_of_loan = st.number_input("Number of Loan", min_value=0)
delay_from_due_date = st.number_input("Delay from Due Date", min_value=0)
num_of_delayed_payment = st.number_input("Number of Delayed Payment", min_value=0)
changed_credit_limit = st.number_input("Changed Credit Limit", min_value=0)
num_credit_inquiries = st.number_input("Number of Credit Inquiries", min_value=0)
outstanding_debt = st.number_input("Outstanding Debt", min_value=0)
credit_utilization_ratio = st.number_input("Credit Utilization Ratio", min_value=0.0)
total_emi_per_month = st.number_input("Total EMI per Month", min_value=0)
amount_invested_monthly = st.number_input("Amount Invested Monthly", min_value=0)
monthly_balance = st.number_input("Monthly Balance", min_value=0)

occupation = st.selectbox("Occupation", ['Scientist', 'Unknown', 'Teacher', 'Engineer', 'Entrepreneur', 'Developer',
 'Lawyer', 'Media_Manager', 'Doctor', 'Journalist', 'Manager', 'Accountant', 'Musician', 'Mechanic', 'Writer', 'Architect'])
month = st.selectbox("Month", ['January', 'July', 'August', 'February', 'March', 'May', 'June', 'April'])
credit_mix = st.selectbox("Credit Mix", [ 'Good', 'Standard', 'Bad'])
payment_of_min_amount = st.selectbox("Payment of Minimum Amount", ['No', 'NM', 'Yes'])
payment_behaviour = st.selectbox("Payment Behaviour", ['High_spent_Small_value_payments', 'Low_spent_Small_value_payments',
 'High_spent_Medium_value_payments', 'High_spent_Large_value_payments', 'Unknown', 'Low_spent_Medium_value_payments',
 'Low_spent_Large_value_payments'])

inputDF = pd.DataFrame(
    {
        'Age' : [age],
        'Annual_Income' : [annual_income],
        'Monthly_Inhand_Income' : [monthly_inhand_income],
        'Number_of_Bank_Accounts' : [num_bank_accounts],
        'Number_of_Credit_Card' : [num_credit_card],
        'Interest_Rate' : [interest_rate],
        'Number_of_Loan' : [num_of_loan],
        'Delay_from_Due_Date' : [delay_from_due_date],
        'Number_of_Delayed_Payment' : [num_of_delayed_payment],
        'Changed_Credit_Limit' : [changed_credit_limit],
        'Number_of_Credit_Inquiries' : [num_credit_inquiries],
        'Outstanding_Debt' : [outstanding_debt],
        'Credit_Utilization_Ratio' : [credit_utilization_ratio],
        'Total_EMI_per_Month' : [total_emi_per_month],
        'Amount_Invested_Monthly' : [amount_invested_monthly],
        'Monthly_Balance' : [monthly_balance],

        'Occupation' : [encoders['Occupation'].transform([occupation])[0]],
        'Month' : [encoders['Month'].transform([month])[0]],
        'Credit_Mix' : [encoders['Credit_Mix'].transform([credit_mix])[0]],
        'Payment_of_Minimum_Amount' : [encoders['Payment_of_Minimum_Amount'].transform([payment_of_min_amount])[0]],
        'Payment_Behaviour' : [encoders['Payment_Behaviour'].transform([payment_behaviour])[0]]
    }
)

if st.button("Predict Credit Score"):
    prediction = model.predict(inputDF)[0]
    
    if prediction == 0:
        st.success("Predicted Credit Score is GOOD")
    elif prediction == 1:
            st.error("Predicted Credit Score is POOR")
    else:
        st.warning("Predicted Credit Score is STANDARD")



# streamlit run app.py >to run the app<