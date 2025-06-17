from src.predictor import CKDPredictor
import streamlit as st

def main():
        # Configure the Streamlit app layout and metadata
    st.set_page_config(page_title="CKD Predictor", page_icon="🧬", layout="wide")
        # App title and description
    st.title("🧬 Chronic Kidney Disease (CKD) Predictor")
    st.markdown("Use this interactive tool to assess the likelihood of CKD based on your medical data.")

    # Sidebar configuration
    with st.sidebar:
        st.markdown("# 🔎 Explore & Predict")
        st.info("Use the checkboxes below to explore the dataset or make a prediction.")
    # Create an instance of the CKDPredictor class
    app = CKDPredictor()

    if not app.df.empty:
        # Create two tabs: one for data analysis, one for prediction
        tab1, tab2 = st.tabs(["📊 Data Exploration", "🩺 CKD Prediction"])
        with tab1:
        # Tab 1: Explore the dataset visually   
            app.data_analysis()
        with tab2:
        # Tab 2: Input medical info and get CKD prediction
            app.form_inputs()

    st.markdown("---")

# Standard Python practice: ensures this code runs only when file is executed directly (not imported)
if __name__ == "__main__":
    main()
