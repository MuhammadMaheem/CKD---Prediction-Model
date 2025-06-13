# CDK---Prediction-Model
 Cronic kidney disease pridiction






About Dataset
Overview

This dataset contains detailed health information for 1,659 patients diagnosed with Chronic Kidney Disease (CKD). The dataset includes demographic details, lifestyle factors, medical history, clinical measurements, medication usage, symptoms, quality of life scores, environmental exposures, and health behaviors. Each patient is uniquely identified by a Patient ID, and the data includes a confidential column indicating the doctor in charge.
Table of Contents

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

Patient Information
Patient ID

    PatientID: A unique identifier assigned to each patient (1 to 1,659).

Demographic Details

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

Lifestyle Factors

    BMI: Body Mass Index of the patients, ranging from 15 to 40.
    Smoking: Smoking status, where 0 indicates No and 1 indicates Yes.
    AlcoholConsumption: Weekly alcohol consumption in units, ranging from 0 to 20.
    PhysicalActivity: Weekly physical activity in hours, ranging from 0 to 10.
    DietQuality: Diet quality score, ranging from 0 to 10.
    SleepQuality: Sleep quality score, ranging from 4 to 10.

Medical History

    FamilyHistoryKidneyDisease: Family history of kidney disease, where 0 indicates No and 1 indicates Yes.
    FamilyHistoryHypertension: Family history of hypertension, where 0 indicates No and 1 indicates Yes.
    FamilyHistoryDiabetes: Family history of diabetes, where 0 indicates No and 1 indicates Yes.
    PreviousAcuteKidneyInjury: History of previous acute kidney injury, where 0 indicates No and 1 indicates Yes.
    UrinaryTractInfections: History of urinary tract infections, where 0 indicates No and 1 indicates Yes.

Clinical Measurements

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

Medications

    ACEInhibitors: Use of ACE inhibitors, where 0 indicates No and 1 indicates Yes.
    Diuretics: Use of diuretics, where 0 indicates No and 1 indicates Yes.
    NSAIDsUse: Frequency of NSAIDs use, ranging from 0 to 10 times per week.
    Statins: Use of statins, where 0 indicates No and 1 indicates Yes.
    AntidiabeticMedications: Use of antidiabetic medications, where 0 indicates No and 1 indicates Yes.

Symptoms and Quality of Life

    Edema: Presence of edema, where 0 indicates No and 1 indicates Yes.
    FatigueLevels: Fatigue levels, ranging from 0 to 10.
    NauseaVomiting: Frequency of nausea and vomiting, ranging from 0 to 7 times per week.
    MuscleCramps: Frequency of muscle cramps, ranging from 0 to 7 times per week.
    Itching: Itching severity, ranging from 0 to 10.
    QualityOfLifeScore: Quality of life score, ranging from 0 to 100.

Environmental and Occupational Exposures

    HeavyMetalsExposure: Exposure to heavy metals, where 0 indicates No and 1 indicates Yes.
    OccupationalExposureChemicals: Occupational exposure to harmful chemicals, where 0 indicates No and 1 indicates Yes.
    WaterQuality: Quality of water, where 0 indicates Good and 1 indicates Poor.

Health Behaviors

    MedicalCheckupsFrequency: Frequency of medical check-ups per year, ranging from 0 to 4.
    MedicationAdherence: Medication adherence score, ranging from 0 to 10.
    HealthLiteracy: Health literacy score, ranging from 0 to 10.

Diagnosis Information

    Diagnosis: Diagnosis status for Chronic Kidney Disease, where 0 indicates No and 1 indicates Yes.

Confidential Information

    DoctorInCharge: This column contains confidential information about the doctor in charge, with "Confidential" as the value for all patients.
    This comprehensive dataset provides valuable insights into the various factors associated with Chronic Kidney Disease and can be used for various analyses, including statistical analysis, machine learning model development, and more.

Dataset Usage and Attribution Notice

This dataset, shared by Rabie El Kharoua, is original and has never been shared before. It is made available under the CC BY 4.0 license, allowing anyone to use the dataset in any form as long as proper citation is given to the author. A DOI is provided for proper referencing. Please note that duplication of this work within Kaggle is not permitted.
Exclusive Synthetic Dataset

This dataset is synthetic and was generated for educational purposes, making it ideal for data science and machine learning projects. It is an original dataset, owned by Mr. Rabie El Kharoua, and has not been previously shared. You are free to use it under the license outlined on the data card. The dataset is offered without any guarantees. Details about the data provider will be shared soon.













About this file

    PatientID: A unique identifier assigned to each patient (1 to 1,659).
    Age: The age of the patients ranges from 20 to 90 years.
    Gender: Gender of the patients, where 0 represents Male and 1 represents Female.
    Ethnicity: The ethnicity of the patients, coded as follows:
        0: Caucasian
        1: African American
        2: Asian
        3: Other
    SocioeconomicStatus: The socioeconomic status of the patients
    EducationLevel: The education level of the patients, coded as follows:
        0: None
        1: High School
        2: Bachelor's
        3: Higher
    BMI: Body Mass Index of the patients, ranging from 15 to 40.
    Smoking: Smoking status, where 0 indicates No and 1 indicates Yes.
    AlcoholConsumption: Weekly alcohol consumption in units, ranging from 0 to 20.
    PhysicalActivity: Weekly physical activity in hours, ranging from 0 to 10.
    DietQuality: Diet quality score, ranging from 0 to 10.
    SleepQuality: Sleep quality score, ranging from 4 to 10.
    FamilyHistoryKidneyDisease: Family history of kidney disease, where 0 indicates No and 1 indicates Yes.
    FamilyHistoryHypertension: Family history of hypertension, where 0 indicates No and 1 indicates Yes.
    FamilyHistoryDiabetes: Family history of diabetes, where 0 indicates No and 1 indicates Yes.
    PreviousAcuteKidneyInjury: History of previous acute kidney injury, where 0 indicates No and 1 indicates Yes.
    UrinaryTractInfections: History of urinary tract infections, where 0 indicates No and 1 indicates Yes.
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
    ACEInhibitors: Use of ACE inhibitors, where 0 indicates No and 1 indicates Yes.
    Diuretics: Use of diuretics, where 0 indicates No and 1 indicates Yes.
    NSAIDsUse: Frequency of NSAIDs use, ranging from 0 to 10 times per week.
    Statins: Use of statins, where 0 indicates No and 1 indicates Yes.
    AntidiabeticMedications: Use of antidiabetic medications, where 0 indicates No and 1 indicates Yes.
    Edema: Presence of edema, where 0 indicates No and 1 indicates Yes.
    FatigueLevels: Fatigue levels, ranging from 0 to 10.
    NauseaVomiting: Frequency of nausea and vomiting, ranging from 0 to 7 times per week.
    MuscleCramps: Frequency of muscle cramps, ranging from 0 to 7 times per week.
    Itching: Itching severity, ranging from 0 to 10.
    QualityOfLifeScore: Quality of life score, ranging from 0 to 100.
    HeavyMetalsExposure: Exposure to heavy metals, where 0 indicates No and 1 indicates Yes.
