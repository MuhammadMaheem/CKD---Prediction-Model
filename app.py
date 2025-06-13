from src.predictor import CKDPredictor
import streamlit as st

def main():
    st.set_page_config(page_title="CKD Predictor", page_icon="🧬", layout="wide")
    st.title("🧬 Chronic Kidney Disease (CKD) Predictor")
    st.markdown("Use this interactive tool to assess the likelihood of CKD based on your medical data.")

    with st.sidebar:
        st.markdown("# 🔎 Explore & Predict")
        st.info("Use the checkboxes below to explore the dataset or make a prediction.")

    app = CKDPredictor()

    if not app.df.empty:
        tab1, tab2 = st.tabs(["📊 Data Exploration", "🩺 CKD Prediction"])
        with tab1:
            app.data_analysis()
        with tab2:
            app.form_inputs()

    st.markdown("---")
    st.markdown("### ℹ️ About")
    st.markdown("""
    This tool uses a machine learning model trained on real-world clinical data to provide predictive insight.
    **Note: This is not a substitute for professional medical advice.**
    """)

if __name__ == "__main__":
    main()
