import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import pickle

# Load the dataset
data = pd.read_csv("transactions.csv")

print("Dataset loaded successfully!")
print(data.head())

# Select input features
X = data[
    [
        "amount",
        "transaction_count",
        "account_age",
        "international"
    ]
]

# Select the target
y = data["is_fraud"]

# Split the data into training and testing
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Create the Random Forest model
model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

# Train the model
model.fit(X_train, y_train)

print("Model trained successfully!")

# Test the model
prediction = model.predict(X_test)

# Calculate accuracy
accuracy = accuracy_score(y_test, prediction)

print("Model Accuracy:", accuracy * 100, "%")

# Save the trained model
with open("fraud_model.pkl", "wb") as file:
    pickle.dump(model, file)

print("Model saved successfully!")