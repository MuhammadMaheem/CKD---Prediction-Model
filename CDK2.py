import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pickle
import os

from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier

@st.cache_resource
def load_model_and_scaler():
    model_path = "ckd_model.pkl"
    scaler_path = "scaler.pkl"
    if not os.path.exists(model_path) or not os.path.exists(scaler_path):
        st.error("Model or scaler file not found. Please ensure both files are in the same directory.")
        return None, None
    model = pickle.load(open(model_path, "rb"))
    scaler = pickle.load(open(scaler_path, "rb"))
    return model, scaler


class CKDPredictor:
    def __init__(self):
        self.model, self.scaler = load_model_and_scaler()
        self.df = pd.read_csv("Chronic_Kidney_Dsease_data.csv")
        self.prepare_data()

    def prepare_data(self):
        self.df.dropna(inplace=True)
        self.df.drop(columns=["PatientID", "DoctorInCharge"], inplace=True)
        return self.df

    def data_analysis(self):
        st.subheader("🔍 Dataset Overview")

        col1, col2 = st.columns(2)
        col1.metric("📦 Total Samples", len(self.df))
        col2.metric("🩺 CKD Cases", int(self.df["Diagnosis"].sum()))

        if st.sidebar.checkbox("Show Data Table"):
            with st.expander("📄 Preview Dataset (Top 5 Rows)"):
                st.dataframe(self.df.head())

        if st.sidebar.checkbox("Show Class Distribution"):
            st.subheader("📊 CKD vs. No CKD Distribution")
            dist = self.df["Diagnosis"].value_counts().sort_index()
            labels = ["No CKD", "CKD"]
            fig1, ax1 = plt.subplots()
            ax1.pie(dist, labels=labels, autopct="%1.1f%%", startangle=90)
            ax1.axis("equal")
            st.pyplot(fig1)

        if st.sidebar.checkbox("Show Summary Statistics"):
            with st.expander("📊 Summary Statistics"):
                st.dataframe(self.df.describe().T)

        if st.sidebar.checkbox("Show Correlation Heatmap"):
            st.subheader("🧠 Feature Correlation Heatmap")
            plt.figure(figsize=(10, 6))
            sns.heatmap(self.df.corr(), annot=True, cmap="coolwarm", fmt=".2f")
            st.pyplot(plt.gcf())

        if st.sidebar.checkbox("Show Feature Distributions"):
            st.subheader("📈 Feature Distribution by CKD Status")
            numeric_cols = self.df.select_dtypes(include=[np.number]).columns.tolist()
            selected_feature = st.selectbox("Select feature for boxplot", numeric_cols)
            fig, ax = plt.subplots()
            sns.boxplot(data=self.df, x="Diagnosis", y=selected_feature, ax=ax)
            ax.set_xticklabels(["No CKD", "CKD"])
            st.pyplot(fig)

        if st.sidebar.checkbox("Feature Importance (if model is tree-based)"):
            if hasattr(self.model, "feature_importances_"):
                importance = self.model.feature_importances_
                
                # Use the same feature list used for training
                feature_names = [
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
                
                imp_df = pd.DataFrame({
                    "Feature": feature_names,
                    "Importance": importance
                }).sort_values("Importance", ascending=False)
                
                fig, ax = plt.subplots(figsize=(10, 5))
                sns.barplot(x="Importance", y="Feature", data=imp_df, ax=ax)
                st.pyplot(fig)
            else:
                st.warning("Feature importance not available for this model.")

        if st.sidebar.checkbox("Download Cleaned Dataset"):
            csv = self.df.to_csv(index=False)
            st.download_button("📥 Download Dataset", data=csv, file_name="cleaned_ckd_dataset.csv", mime="text/csv")

    def form_inputs(self):
        st.subheader("🩺 Enter Your Medical Information")
 
        inputs = {}

        with st.form("ckd_form"):
            col1, col2 = st.columns(2)

            with col1:
                inputs["age"] = st.number_input("Age (years)", 1, 100, 45)
                inputs["BMI"] = st.number_input("BMI (Body Mass Index))", 15, 39, 18)
                inputs["systolic_bp"] = st.number_input("Systolic Blood Pressure (mmHg)", 90, 179, 90)
                inputs["diastolic_bp"] = st.number_input("Diastolic Blood Pressure (mmHg)", 60, 119, 70)
                inputs["fasting_blood_sugar"] = st.number_input("Fasting Blood Sugar (mg/dL)", 70, 199, 80)
                inputs["hba1c"] = st.number_input("HbA1c (%)",4 , 9, 6)

            with col2:
                inputs["serum_creatinine"] = st.number_input("Serum Creatinine (mg/dL)", 0.0, 4.9, 3.0)
                inputs["bun"] = st.number_input("BUN Levels (mg/dL))", 5.0, 49.9, 5.0)
                inputs["gfr"] = st.number_input("GFR (mL/min/1.73m²)", 15, 119, 15)
                inputs["protein_in_urine"] = st.number_input("Protein in Urine)", 0.0, 4.9, 0.0)
                inputs["hemoglobin"] = st.number_input("Hemoglobin Level (g/dL)", 10.0, 17.9, 10.0)
                inputs["cholesterol"] = st.number_input("Cholesterol Total (mg/dL)", 150, 299, 150)

            submitted = st.form_submit_button("🔍 Predict CKD")

        if submitted:
            input_array = np.array(list(inputs.values())).reshape(1, -1)
            input_scaled = self.scaler.transform(input_array)

            prediction = self.model.predict(input_scaled)[0]
            try:
                confidence = self.model.decision_function(input_scaled)[0]
                prob = round(1 / (1 + np.exp(-confidence)), 2)
            except:
                prob = "Unavailable"

            st.markdown("---")
            st.subheader("📋 Prediction Result")

            if prediction == 1:
                st.error("⚠️ The model predicts that you **may have CKD**.")
            else:
                st.success("✅ The model predicts that you **likely do NOT have CKD**.")

            st.info(f"🧠 Model Confidence (estimated): `{prob}`")


# Main App Entry
def main():
    st.set_page_config(page_title="CKD Predictor", page_icon="🧬", layout="wide")

    st.title("🧬 Chronic Kidney Disease (CKD) Predictor")
    st.markdown("Use this interactive tool to assess the likelihood of Chronic Kidney Disease based on your medical values.")

    with st.sidebar:
        st.image("https://i.imgur.com/4HJbzEq.png", width=150)
        st.markdown("## 🔎 Explore & Predict")
        st.markdown("Use the checkboxes below to explore the dataset or make a prediction.")
        st.info("This tool is for educational purposes only and should not replace medical advice.")

    app = CKDPredictor()

    tab1, tab2 = st.tabs(["📊 Data Exploration", "🩺 CKD Prediction"])

    with tab1:
        app.data_analysis()

    with tab2:
        app.form_inputs()

    st.markdown("---")
    st.markdown("### ℹ️ About")
    st.markdown("""
    **Chronic Kidney Disease (CKD)** is a condition where the kidneys lose function over time. 
    This app uses a machine learning model trained on clinical data to provide predictive support. 
    **Please consult a medical professional for real diagnosis.**
    """)
    st.caption("👨‍⚕️ Created with ❤️ using Streamlit | Model: SVM | Developer: [Your Name]")


if __name__ == "__main__":
    main()
