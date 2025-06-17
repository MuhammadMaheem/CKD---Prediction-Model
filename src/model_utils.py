import pickle # For loading serialized model and scaler
import os # For file path checks
import streamlit as st # For UI feedback in case of missing files   

@st.cache_resource
def load_model_and_scaler():
    """
    Loads the pre-trained CKD prediction model and its corresponding scaler.
    This function is cached by Streamlit to avoid reloading on every rerun.

    Returns:
        tuple: (model, scaler) if files exist, else (None, None)
    """
    model_path = "models/ckd_model.pkl"
    scaler_path = "models/scaler.pkl"
    
    if not os.path.exists(model_path) or not os.path.exists(scaler_path):
        st.error("Model or scaler file not found in 'models/' directory.")
        return None, None

    with open(model_path, "rb") as f:
        model = pickle.load(f)
    with open(scaler_path, "rb") as f:
        scaler = pickle.load(f)

    return model, scaler
