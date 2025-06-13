import pickle
import os
import streamlit as st

@st.cache_resource
def load_model_and_scaler():
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
