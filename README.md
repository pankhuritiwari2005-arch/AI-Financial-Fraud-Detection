#  AI-Powered Financial Fraud Detection System

##  Project Description

This project is an AI-powered Financial Fraud Detection System developed using Python and Machine Learning.

The system analyze financial transaction details and predicts whether a transaction is **Fraudulent** or **Legitimate**.

A Machine Learning model is trained using transaction data and integrated with a simple Streamlit web application.

##  Objectives

- Detect suspicious financial transactions.
- Use Machine Learning for fraud prediction.
- Provide a simple and easy-to-use web interface.
- Help identify potentially fraudulent transactions quickly.

##  Technologies Used

- Python
- Pandas
- Scikit-learn
- Streamlit
- Machine Learning
- CSV Dataset

##  Project Files

- app.py – Streamlit web application
- train_model.py – Code for training the Machine Learning model
- transactions.csv – Transaction dataset
- fraud_model.pkl – Trained Machine Learning model

##  How to Run the Project

     1. How to Run the Project


-pip install pandas scikit-learn streamlit

     2. Train the model


-python train_model.py

     3. Run the streamlit application


 -python -m streamlit run app.py


     4. Open the application


 -http://localhost:8501 

##  How it Works

1. Transaction data is provided  to the system.
2. The trained Machine Learning model analyzes the transaction.
3. The system predicts the transaction status.\
4. The result is displayed as:
   . Fraudulent Transaction
   . Legitimate Transaction
