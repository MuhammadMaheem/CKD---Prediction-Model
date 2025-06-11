import pandas as pd
import numpy as np
import pickle
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score

# Load dataset
df = pd.read_csv("Chronic_Kidney_Dsease_data.csv")

# Strip whitespace in column names
df.columns = df.columns.str.strip()

# Fix target inconsistencies
df['Diagnosis'] = df['Diagnosis'].replace({'CKD': 1, 'Not CKD': 0})

# Fill missing values
for col in df.columns:
    if df[col].dtype == 'object' and col != 'Diagnosis':
        df[col] = df[col].fillna(df[col].mode()[0])
    elif col != 'Diagnosis':
        df[col] = df[col].fillna(df[col].median())

# If any categorical columns remain, encode them (except target)
categorical_cols = df.select_dtypes(include='object').columns.tolist()
if 'Diagnosis' in categorical_cols:
    categorical_cols.remove('Diagnosis')

for col in categorical_cols:
    le = LabelEncoder()
    df[col] = le.fit_transform(df[col])

# Select 12 features for your model
features = [
    "Age",
    "BMI",
    "SystolicBP",
    "DiastolicBP",
    "FastingBloodSugar",
    "HbA1c",
    "SerumCreatinine",
    "BUNLevels",
    "GFR",
    "ProteinInUrine",
    "HemoglobinLevels",
    "CholesterolTotal"
]

# Check if all features exist
missing_cols = [f for f in features if f not in df.columns]
if missing_cols:
    raise ValueError(f"Missing columns in dataset: {missing_cols}")

X = df[features]
y = df["Diagnosis"].astype(int)

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Scale features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Train Random Forest Classifier
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train_scaled, y_train)

# Predictions & evaluation
y_pred = model.predict(X_test_scaled)
print("Accuracy:", accuracy_score(y_test, y_pred))
print("Classification Report:\n", classification_report(y_test, y_pred))

# Save model and scaler for later use
with open("ckd_model.pkl", "wb") as f:
    pickle.dump(model, f)

with open("scaler.pkl", "wb") as f:
    pickle.dump(scaler, f)

print("Model and scaler saved successfully.")
