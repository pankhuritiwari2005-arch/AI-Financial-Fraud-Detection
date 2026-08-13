import streamlit as st
import pickle

# Load the trained AI model
with open("fraud_model.pkl", "rb") as file:
    model = pickle.load(file)

# Page title
st.title("💳 AI-Powered Financial Fraud Detection System")

st.write("Enter the transaction details below to check for fraud.")

# Transaction amount
amount = st.number_input(
    "Transaction Amount (₹)",
    min_value=0.0,
    value=1000.0
)

# Number of recent transactions
transaction_count = st.number_input(
    "Number of Recent Transactions",
    min_value=0,
    value=2
)

# Account age
account_age = st.number_input(
    "Account Age (Years)",
    min_value=0,
    value=5
)

# International transaction
international = st.selectbox(
    "Is this an International Transaction?",
    ["No", "Yes"]
)

# Check button
if st.button("🔍 Check Transaction"):

    # Convert Yes/No to 1/0
    if international == "Yes":
        international_value = 1
    else:
        international_value = 0

    # Prepare transaction data
    transaction = [[
        amount,
        transaction_count,
        account_age,
        international_value
    ]]

    # AI prediction
    prediction = model.predict(transaction)

    # Fraud probability
    probability = model.predict_proba(transaction)

    fraud_probability = probability[0][1] * 100

    # Display probability
    st.subheader("Result")

    st.write(
        "Fraud Probability:",
        round(fraud_probability, 2),
        "%"
    )

    # Display result
    if prediction[0] == 1:

        st.error("🚨 FRAUDULENT TRANSACTION DETECTED!")

        st.warning(
            "Please verify this transaction immediately."
        )

    else:

        st.success("✅ LEGITIMATE TRANSACTION")

        st.info(
            "No suspicious activity detected."
        )