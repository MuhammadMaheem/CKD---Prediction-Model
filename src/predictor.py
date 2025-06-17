# predictor.py
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os
from src.model_utils import load_model_and_scaler

class CKDPredictor:
    def __init__(self):
        """
        Initializes the CKDPredictor class:
        - Loads the pre-trained machine learning model and scaler using a utility function.
        - Loads the dataset and prepares it for analysis.
        """

        self.model, self.scaler = load_model_and_scaler()
        self.data_path = "data/Chronic_Kidney_Dsease_data.csv"
        if not os.path.exists(self.data_path):
            st.error("Dataset file not found in 'data/' directory.")
            self.df = pd.DataFrame()
        else:
            self.df = pd.read_csv(self.data_path)
            self.prepare_data()

    def prepare_data(self):
        """
        Cleans the dataset by:
        - Removing rows with missing values.
        - Dropping irrelevant columns such as 'PatientID' and 'DoctorInCharge'.
        """
        self.df.dropna(inplace=True)
        self.df.drop(columns=[col for col in ["PatientID", "DoctorInCharge"] if col in self.df.columns], inplace=True)

    def bin_feature(self, series, bins=5):
        """
        Safely bins a numeric series with unique string labels.
        Automatically handles duplicate values or irregular spreads.
        """
        if series.nunique() <= 1:
            return pd.Series(["Only one value"] * len(series), index=series.index)

        try:
            binned = pd.qcut(series, q=bins, duplicates='drop')
        except ValueError:
            binned = pd.cut(series, bins=bins)

        # Recreate labels for clarity
        bin_labels = [f"{round(l, 1)} - {round(r, 1)}" for l, r in zip(binned.cat.categories.left, binned.cat.categories.right)]
        return pd.cut(series, bins=binned.cat.categories, labels=bin_labels, include_lowest=True)

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

        if st.sidebar.checkbox("Show Feature Distributions"):
            st.subheader("📈 Feature Distribution by CKD Status")
            numeric_cols = self.df.select_dtypes(include=[np.number]).columns.tolist()
            selected_feature = st.selectbox("Select feature for boxplot", numeric_cols)
            fig, ax = plt.subplots()
            sns.boxplot(data=self.df, x="Diagnosis", y=selected_feature, ax=ax)
            ax.set_xticklabels(["No CKD", "CKD"])
            st.pyplot(fig)

        if st.sidebar.checkbox("📊 CKD vs No CKD by Binned Features"):
            st.subheader("🧮 Compare CKD Distribution Across Feature Ranges")
            numeric_cols = self.df.select_dtypes(include=[np.number]).columns.tolist()
            selected_feature = st.selectbox("Select feature to bin and visualize", numeric_cols, key="binning")

            binned_series = self.bin_feature(self.df[selected_feature], bins=5)
            binned_df = pd.DataFrame({
                "Binned": binned_series,
                "Diagnosis": self.df["Diagnosis"]
            })

            ct = pd.crosstab(binned_df["Binned"], binned_df["Diagnosis"])
            ct.columns = ["No CKD", "CKD"]
            ct = ct.sort_index()

            fig, ax = plt.subplots()
            ct.plot(kind="bar", stacked=True, ax=ax, color=["skyblue", "salmon"])
            ax.set_title(f"CKD vs No CKD by {selected_feature} Ranges")
            ax.set_xlabel(f"{selected_feature} Ranges")
            ax.set_ylabel("Count")
            st.pyplot(fig)

        if st.sidebar.checkbox("Feature Importance (if model is tree-based)"):
            if hasattr(self.model, "feature_importances_"):
                importance = self.model.feature_importances_
                feature_names = [
                    "Age", "BMI", "SystolicBP", "DiastolicBP", "FastingBloodSugar", "HbA1c",
                    "SerumCreatinine", "BUNLevels", "GFR", "ProteinInUrine", "HemoglobinLevels", "CholesterolTotal"
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
   
    def form_inputs(self):
        st.subheader("🩺 Enter Your Medical Information")
        inputs = {}

        with st.form("ckd_form"):
            col1, col2 = st.columns(2)
            with col1:
                inputs["Age"] = st.number_input("Age (years)", 1, 100, 45)
                inputs["BMI"] = st.number_input("BMI (Body Mass Index)", 15, 39, 18)
                inputs["SystolicBP"] = st.number_input("Systolic Blood Pressure (mmHg)", 90, 179, 90)
                inputs["DiastolicBP"] = st.number_input("Diastolic Blood Pressure (mmHg)", 60, 119, 70)
                inputs["FastingBloodSugar"] = st.number_input("Fasting Blood Sugar (mg/dL)", 70, 199, 80)
                inputs["HbA1c"] = st.number_input("HbA1c (%)", 4.0, 9.0, 6.0)

            with col2:
                inputs["SerumCreatinine"] = st.number_input("Serum Creatinine (mg/dL)", 0.0, 4.9, 3.0)
                inputs["BUNLevels"] = st.number_input("BUN Levels (mg/dL)", 5.0, 49.9, 5.0)
                inputs["GFR"] = st.number_input("GFR (mL/min/1.73m²)", 15, 119, 15)
                inputs["ProteinInUrine"] = st.number_input("Protein in Urine", 0.0, 4.9, 0.0)
                inputs["HemoglobinLevels"] = st.number_input("Hemoglobin Level (g/dL)", 10.0, 17.9, 10.0)
                inputs["CholesterolTotal"] = st.number_input("Cholesterol Total (mg/dL)", 150, 299, 150)

            submitted = st.form_submit_button("🔍 Predict CKD")

        if submitted and self.model is not None:
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

