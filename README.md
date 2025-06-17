
# 🧬 Chronic Kidney Disease (CKD) Predictor App - Case Study

An interactive machine learning web app using **Streamlit** to predict Chronic Kidney Disease (CKD) from medical features.

---
You can View it on Github: [GitHub Link CKD](https://github.com/MuhammadMaheem/CDK---Prediction-Model)

You can also View the Live Demo on streamlit app: [StreamLit app](https://ckd-prediction-model-sfyp.streamlit.app/)

---

## About Dataset
### Overview

This dataset contains detailed health information for 1,659 patients diagnosed with Chronic Kidney Disease (CKD). The dataset includes demographic details, lifestyle factors, medical history, clinical measurements, medication usage, symptoms, quality of life scores, environmental exposures, and health behaviors. Each patient is uniquely identified by a Patient ID, and the data includes a confidential column indicating the doctor in charge.
### Table of Contents

    Patient Information
        Patient ID
        Demographic Details
        Lifestyle Factors
    Medical History
    Clinical Measurements
    Medications
    Symptoms and Quality of Life
    Environmental and Occupational Exposures
    Health Behaviors
    Diagnosis Information

### Patient Information
Patient ID

    PatientID: A unique identifier assigned to each patient (1 to 1,659).

### Demographic Details

    Age: The age of the patients ranges from 20 to 90 years.
    Gender: Gender of the patients, where 0 represents Male and 1 represents Female.
    Ethnicity: The ethnicity of the patients, coded as follows:
        0: Caucasian
        1: African American
        2: Asian
        3: Other
    SocioeconomicStatus: The socioeconomic status of the patients, coded as follows:
        0: Low
        1: Middle
        2: High
    EducationLevel: The education level of the patients, coded as follows:
        0: None
        1: High School
        2: Bachelor's
        3: Higher

### Lifestyle Factors

    BMI: Body Mass Index of the patients, ranging from 15 to 40.
    Smoking: Smoking status, where 0 indicates No and 1 indicates Yes.
    AlcoholConsumption: Weekly alcohol consumption in units, ranging from 0 to 20.
    PhysicalActivity: Weekly physical activity in hours, ranging from 0 to 10.
    DietQuality: Diet quality score, ranging from 0 to 10.
    SleepQuality: Sleep quality score, ranging from 4 to 10.

### Medical History

    FamilyHistoryKidneyDisease: Family history of kidney disease, where 0 indicates No and 1 indicates Yes.
    FamilyHistoryHypertension: Family history of hypertension, where 0 indicates No and 1 indicates Yes.
    FamilyHistoryDiabetes: Family history of diabetes, where 0 indicates No and 1 indicates Yes.
    PreviousAcuteKidneyInjury: History of previous acute kidney injury, where 0 indicates No and 1 indicates Yes.
    UrinaryTractInfections: History of urinary tract infections, where 0 indicates No and 1 indicates Yes.

### Clinical Measurements

    SystolicBP: Systolic blood pressure, ranging from 90 to 180 mmHg.
    DiastolicBP: Diastolic blood pressure, ranging from 60 to 120 mmHg.
    FastingBloodSugar: Fasting blood sugar levels, ranging from 70 to 200 mg/dL.
    HbA1c: Hemoglobin A1c levels, ranging from 4.0% to 10.0%.
    SerumCreatinine: Serum creatinine levels, ranging from 0.5 to 5.0 mg/dL.
    BUNLevels: Blood Urea Nitrogen levels, ranging from 5 to 50 mg/dL.
    GFR: Glomerular Filtration Rate, ranging from 15 to 120 mL/min/1.73 m².
    ProteinInUrine: Protein levels in urine, ranging from 0 to 5 g/day.
    ACR: Albumin-to-Creatinine Ratio, ranging from 0 to 300 mg/g.
    SerumElectrolytesSodium: Serum sodium levels, ranging from 135 to 145 mEq/L.
    SerumElectrolytesPotassium: Serum potassium levels, ranging from 3.5 to 5.5 mEq/L.
    SerumElectrolytesCalcium: Serum calcium levels, ranging from 8.5 to 10.5 mg/dL.
    SerumElectrolytesPhosphorus: Serum phosphorus levels, ranging from 2.5 to 4.5 mg/dL.
    HemoglobinLevels: Hemoglobin levels, ranging from 10 to 18 g/dL.
    CholesterolTotal: Total cholesterol levels, ranging from 150 to 300 mg/dL.
    CholesterolLDL: Low-density lipoprotein cholesterol levels, ranging from 50 to 200 mg/dL.
    CholesterolHDL: High-density lipoprotein cholesterol levels, ranging from 20 to 100 mg/dL.
    CholesterolTriglycerides: Triglycerides levels, ranging from 50 to 400 mg/dL.

### Medications

    ACEInhibitors: Use of ACE inhibitors, where 0 indicates No and 1 indicates Yes.
    Diuretics: Use of diuretics, where 0 indicates No and 1 indicates Yes.
    NSAIDsUse: Frequency of NSAIDs use, ranging from 0 to 10 times per week.
    Statins: Use of statins, where 0 indicates No and 1 indicates Yes.
    AntidiabeticMedications: Use of antidiabetic medications, where 0 indicates No and 1 indicates Yes.

### Symptoms and Quality of Life

    Edema: Presence of edema, where 0 indicates No and 1 indicates Yes.
    FatigueLevels: Fatigue levels, ranging from 0 to 10.
    NauseaVomiting: Frequency of nausea and vomiting, ranging from 0 to 7 times per week.
    MuscleCramps: Frequency of muscle cramps, ranging from 0 to 7 times per week.
    Itching: Itching severity, ranging from 0 to 10.
    QualityOfLifeScore: Quality of life score, ranging from 0 to 100.

### Environmental and Occupational Exposures

    HeavyMetalsExposure: Exposure to heavy metals, where 0 indicates No and 1 indicates Yes.
    OccupationalExposureChemicals: Occupational exposure to harmful chemicals, where 0 indicates No and 1 indicates Yes.
    WaterQuality: Quality of water, where 0 indicates Good and 1 indicates Poor.

### Health Behaviors

    MedicalCheckupsFrequency: Frequency of medical check-ups per year, ranging from 0 to 4.
    MedicationAdherence: Medication adherence score, ranging from 0 to 10.
    HealthLiteracy: Health literacy score, ranging from 0 to 10.

### Diagnosis Information

    Diagnosis: Diagnosis status for Chronic Kidney Disease, where 0 indicates No and 1 indicates Yes.

### Confidential Information

    DoctorInCharge: This column contains confidential information about the doctor in charge, with "Confidential" as the value for all patients.
    This comprehensive dataset provides valuable insights into the various factors associated with Chronic Kidney Disease and can be used for various analyses, including statistical analysis, machine learning model development, and more.




---

## 📁 Project Structure

```
ckd_predictor_app/
├── app.py                  # Main Streamlit app
├── requirements.txt        # Required Python packages
│
├── data/
│   └── Chronic_Kidney_Dsease_data.csv  # Dataset
│
├── models/
│   ├── train_model.py      # Model training script
│   ├── ckd_model.pkl       # Trained Random Forest model
│   └── scaler.pkl          # Trained StandardScaler object
│
├── src/
│   ├── __init__.py         # Python module marker
│   ├── predictor.py        # Core app logic (CKDPredictor class)
│   └── utils.py            # Utility functions (model loader)
```

---

## 📦 Dependencies

List of all required libraries:

- `streamlit`: Web UI
- `pandas`: Data processing
- `numpy`: Numerical calculations
- `scikit-learn`: ML model training
- `matplotlib`, `seaborn`: Visualization
- `pickle`: Save/load model and scaler

Install them with:

```
pip install -r requirements.txt
```

---

## 📄 `app.py` — Main Entry Point

### Purpose

Runs the Streamlit app, sets layout, and routes to data exploration or CKD prediction.

### Key Functions

- `st.set_page_config()`: Set page title, icon, layout
- Tabs: 
  - **📊 Data Exploration**
  - **🩺 CKD Prediction**
- Initializes `CKDPredictor` class
- Checks if dataset is loaded before proceeding

---

## 📄 `src/__init__.py`

### Purpose

Marks the `src/` directory as a Python module.

---

## 📄 `src/utils.py`

### Function: `load_model_and_scaler()`

**What it does**:
- Loads `ckd_model.pkl` and `scaler.pkl`
- Checks if files exist
- Returns the model and scaler
- Cached using `@st.cache_resource` for performance

---

## 📄 `src/predictor.py`

### Class: `CKDPredictor`

Main class that handles:
- Dataset loading & cleaning
- Data exploration
- Form input & prediction

---

### `__init__()`

- Loads model and scaler
- Reads dataset `Chronic_Kidney_Dsease_data.csv`
- Drops irrelevant columns
- Prepares clean DataFrame

---

### `prepare_data()`

- Drops missing rows
- Drops `PatientID`, `DoctorInCharge` columns if found (because in ML they are unasessary coloums)

---

### `data_analysis()`

Provides multiple interactive analysis options:

1. **Dataset Info**
   - Total samples
   - Total CKD cases

2. **Show Data Table**
   - Displays first 5 rows

3. **Class Distribution**
   - Pie chart of CKD vs No CKD

4. **Summary Statistics**
   - Shows `describe().T` of features

5. **Feature Distribution**
   - Boxplot by CKD status (selectable)

6. **Feature Importance**
   - Shows bar chart if model has `feature_importances_`

7. **Download Button**
   - Allows downloading cleaned dataset

---

### `form_inputs()`

Interactive patient form to collect 12 features:
Because these 12 features plays a major roll in CKD

- Age
- BMI
- SystolicBP
- DiastolicBP
- FastingBloodSugar
- HbA1c
- SerumCreatinine
- BUNLevels
- GFR
- ProteinInUrine
- HemoglobinLevels
- CholesterolTotal

### On submission:

- Scales inputs using loaded `StandardScaler`
- Predicts using `RandomForestClassifier`
- Shows result: CKD or No CKD
- Optionally shows model confidence

---

## 📄 `models/train_model.py`

### Purpose

Train and save the CKD prediction model and scaler.

---

### Steps Performed

1. **Load Data**
   - `pandas.read_csv()`

2. **Data Prepareing**
   - Droping "PatientID" and "DoctorInCharge" (becuase they are useless in prediction)

3. **Target Column Cleanup**
   - Replace `CKD` with `1`, `Not CKD` with `0`



4. **Select Features**
   ```
   [
     "Age", "BMI", "SystolicBP", "DiastolicBP", "FastingBloodSugar",
     "HbA1c", "SerumCreatinine", "BUNLevels", "GFR", "ProteinInUrine",
     "HemoglobinLevels", "CholesterolTotal"
   ]
   ```
    Age: The age of the patients ranges from 20 to 90 years.
    
    BMI: Body Mass Index of the patients, ranging from 15 to 40.
    
    SystolicBP: Systolic blood pressure, ranging from 90 to 180 mmHg.
    
    DiastolicBP: Diastolic blood pressure, ranging from 60 to 120 mmHg.
    
    FastingBloodSugar: Fasting blood sugar levels, ranging from 70 to 200 mg/dL.
    
    HbA1c: Hemoglobin A1c levels, ranging from 4.0% to 10.0%.
    
    SerumCreatinine: Serum creatinine levels, ranging from 0.5 to 5.0 mg/dL.
    
    BUNLevels: Blood Urea Nitrogen levels, ranging from 5 to 50 mg/dL.
    
    GFR: Glomerular Filtration Rate, ranging from 15 to 120 mL/min/1.73 m².
    
    ProteinInUrine: Protein levels in urine, ranging from 0 to 5 g/day.
    
    HemoglobinLevels: Hemoglobin levels, ranging from 10 to 18 g/dL.

    CholesterolTotal: Total cholesterol levels, ranging from 150 to 300 mg/dL.


7. **Train-Test Split**
   - 80/20 split

8. **Standard Scaling**
   - StandardScaler transforms features to have:
    Mean = 0   
    Standard deviation = 1

Helps models learn better, especially when features vary in range.

1. **Train Model**
   - Random Forest Classifier
      -A Random Forest Classifier is trained with 100 trees.
         It's robust, handles both linear and non-linear data well, and is good for medical tasks.

2.  **Evaluate**
    - Accuracy and classification report

3.  **Save Artifacts**
    - `ckd_model.pkl`
    - `scaler.pkl`

---

## 📄 `data/Chronic_Kidney_Dsease_data.csv`

- Original CKD dataset.
- Contains medical features and diagnosis column.
- Preprocessed in `train_model.py`.

---

## 🧪 Evaluation Metrics

Sample result from training:

```
Accuracy: 0.96
Classification Report:
              precision    recall  f1-score   support

           0       0.95      0.98      0.96       50
           1       0.98      0.94      0.96       50
```

---

## ▶️ How to Run the App

```bash
streamlit run app.py
```

**Make sure:**
- `ckd_model.pkl` and `scaler.pkl` exist in `models/`
- Dataset exists in `data/`

---


## ✅ Summary

- Uses ML and Streamlit for an intuitive CKD prediction tool
- Modular codebase (train, utils, logic, UI)
- Real dataset-based training
- Live feedback with charts, summaries, and results
