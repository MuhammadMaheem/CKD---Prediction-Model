import streamlit as st                 # For building the interactive web interface
import pandas as pd                   # For data manipulation
import numpy as np                    # For numerical operations
import pickle                         # For saving and loading models
import os                             # For file path operations
import seaborn as sns                 # For data visualization (heatmap, pairplot, etc.)
import matplotlib.pyplot as plt       # For plotting graphs
from sklearn.model_selection import train_test_split   # For splitting data into train/test sets
from sklearn.preprocessing import StandardScaler       # For scaling input features
from sklearn.pipeline import Pipeline                  # For chaining preprocessing and model steps
from sklearn.svm import SVC                            # SVM Classifier for predictions





# Caches the loaded data so it doesn’t reload every time
@st.cache_data
def data_loading_for_st():
    """
----------------------------------------------------------
    Function: data_loading_for_st

    Loads CKD dataset from CSV.
    Drops non-useful columns like PatientID and DoctorInCharge.
----------------------------------------------------------

    Returns:
    df : DataFrame
        Processed dataset ready for training or analysis
----------------------------------------------------------

    """

    df = pd.read_csv("Chronic_Kidney_Dsease_data.csv")
    df = df.drop(columns=["PatientID","DoctorInCharge"])
    return df


# Caches or trains and saves the model pipeline
@st.cache_resource
def train_load_and_save_model(df,model_path,selected_features):

    """
----------------------------------------------------------

    Function: train_load_and_save_model
    Loads a pre-trained model if exists; else trains and saves a new model.
----------------------------------------------------------
    Parameters:   

    Splits data into features (X) and target (y = Diagnosis)
    Train/Test split (80/20) with diagnosis class
    with open(model_path, "rb") as file:: Opens the file in read-binary mode.
    selected_features : list - features used in training
    Pipline : StandardScaler: normalizes features | SVC: Support Vector Classifier with RBF kernel
----------------------------------------------------------

    Returns:
----------------------------------------------------------
    pipeline :  Returns the loaded model immediately
----------------------------------------------------------

    """



    if os.path.exists(model_path):
        with open(model_path,"rb") as file:
            return pickle.load(file)
    X = df[selected_features]
    y = df["Diagnosis"]
    X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2,stratify=y, random_state=42)

    pipeline = Pipeline([
        ("scalar", StandardScaler()),
        ("svm", SVC(kernel="rbf",C=1.0,gamma="scale",random_state=42))
    ])
    pipeline.fit(X_train,y_train)

    with open(model_path,"wb") as file:
        pickle.dump(pipeline,file)
    return pipeline




# Class that handles prediction and data visualization logic
class CDKPredictor:

    # CKD = Chronic Kidney Disease

    def __init__(self):
        """

----------------------------------------------------------
        -> Path to the saved model   
        -> Selected features ["Age", "BMI", "SystolicBP", "DiastolicBP", "SerumCreatinine",
            "GFR", "BUNLevels", "ProteinInUrine", "FastingBloodSugar", "HbA1c"] ----> used for training and prediction
        
----------------------------------------------------------
        -> Loads dataset and trains/loads model using earlier functions.
----------------------------------------------------------

         """

        self.model_path = "svm_ckd_model.pkl"
        self.seleted_features = [
            "Age", "BMI", "SystolicBP", "DiastolicBP", "SerumCreatinine",
            "GFR", "BUNLevels", "ProteinInUrine", "FastingBloodSugar", "HbA1c"
        ]
        self.df = data_loading_for_st()
        self.model = train_load_and_save_model(self.df, self.model_path,self.seleted_features)




    def data_analysis(self):
        """
----------------------------------------------------------
    -> Understanding the Data and showing it on Streamlit
    -> Showing the Heading "Understanding The Data"
----------------------------------------------------------
    -> Checkbox Triggers and shows the "Data Preview"
    -> Displays a subheader "Show Data Table"
    -> Shows the first 5 rows of the dataset using st.dataframe(self.df.head()).
----------------------------------------------------------
    -> Checkbox triggers the display of a Seaborn heatmap.
    -> select_dtypes(include=[np.number]) filters only numeric columns.
    -> .corr() calculates correlation between those columns.
    -> annot=True shows the correlation values in each cell.
    -> coolwarm color scheme highlights positive and negative correlations.
    -> st.pyplot(plt.gcf()) displays the plot in Streamlit.
    -> plt.clf() clears the figure after showing it to avoid overlapping in future plots.

----------------------------------------------------------
    -> Displays scatterplot matrix (pairplot) for selected features: ["Age", "GFR", "SerumCreatinine", "HbA1c", "Diagnosis"]
    -> Colors the points based on the "Diagnosis" column (using hue). 
    -> Helps understand the relationships between features grouped by diagnosis.
----------------------------------------------------------
    -> Creates a bar chart of how many samples belong to each class (CKD or not).
    -> Uses Seaborn's countplot() to show frequency counts for the "Diagnosis" column.

----------------------------------------------------------


    
    
    
    
    """
        st.sidebar.header("Understanding The Data")

        if st.sidebar.checkbox("Show Data Table"):
            st.subheader("Data Preview O.o")
            st.dataframe(self.df.head())
        
        
        if st.sidebar.checkbox("Show Corelation Heatmap"):
            st.subheader("Correlation Heatmap X_x")
            plt.figure(figsize=(26,22))
            sns.heatmap(self.df.select_dtypes(include=[np.number]).corr(), annot=True, cmap="coolwarm")
            st.pyplot(plt.gcf())
            plt.clf()


        if st.sidebar.checkbox("Show Pair Plot (selected Features "):
            st.subheader("Pair Plot ;* ")
            st.markdown("This shows relationship of grouped data by CDK diagonosis")
            pair_df = self.df[["Age", "GFR", "SerumCreatinine", "HbA1c", "Diagnosis"]]
            sns.pairplot(pair_df,hue="Diagnosis")
            st.pyplot(plt.gcf())
            plt.clf()

        
        if st.sidebar.checkbox("Show Class Distribution"):
            st.subheader("Diagnosis Distribution -_-")
            sns.countplot(x="Diagnosis", data= self.df)
            st.pyplot(plt.gcf())
            plt.clf()

    






    def form_inputs(self):
    
        """
----------------------------------------------------------
    Displays a form to input medical values needed by the model.
    Dynamically creates number input fields for each feature in a loop:
----------------------------------------------------------

    Loops through each feature in fields.
    Dynamically creates a number input box in Streamlit with:
    Label = feature name
    Minimum and maximum value range
    Default value = midpoint of the range
    Format = two decimal places
    Stores the user inputs in the inputs dictionary.
----------------------------------------------------------
    
    On clicking "Predict CDK" button:
    Gathers all input values.
    Converts them to a NumPy array of shape (1, n_features).
    Passes them to self.model (pre-loaded trained model) for prediction.
    Displays result:
        st.error("You have CDK :( ") if prediction == 1
        st.success("You don't have CDK :)") if prediction == 0
----------------------------------------------------------
        """

    
        st.header("Input Medical Values ^ ^ ")
        inputs = {}
        fields = {
            "Age": (0, 120),
            "BMI": (10.0, 50.0),
            "SystolicBP": (80, 200),
            "DiastolicBP": (40, 130),
            "SerumCreatinine": (0.1, 15.0),
            "GFR": (0.0, 150.0),
            "BUNLevels": (1.0, 100.0),
            "ProteinInUrine": (0.0, 10.0),
            "FastingBloodSugar": (50, 300),
            "HbA1c": (3.0, 15.0)

        }
        # Creating input fields dynamically
        for feature, (min_val , max_val) in fields.items():
            default_Value = round((float(min_val) + float(max_val)) / 2,1)
            inputs[feature] = st.number_input(
                f"{feature}",
                min_value = float(min_val),
                max_value = float(max_val),
                value= float(default_Value),
                format="%.2f"
            )
        if st.button("Predict CDK"):
            input_array = np.array(list(inputs.values())).reshape(1,-1)
            prediction = self.model.predict(input_array)[0]
            if prediction == 1:
                st.error("You have CDK (Chronic Kidney Disease). :( ")
            else:
                st.success("You don't have CDK (Chronic Kidney Disease). :)")




# Entry point for the Streamlit app

def main():
    """
----------------------------------------------------------
    Displays main app title and description.    
    Instantiates the CDKPredictor class.
    Calls data_analysis() to display optional plots.
    Calls form_inputs() to handle user prediction inputs.

----------------------------------------------------------
    
    if __name__ == "__main__":
    Ensures that the app only runs when the script is executed directly (not imported as a module).
----------------------------------------------------------
    """

    st.title("Chronic Kidney Disease Predictor")
    st.markdown("Enter your medical values to check the if you have CDK or not")


    app = CDKPredictor()
    app.data_analysis()
    app.form_inputs()

if __name__ == "__main__":
    # Run the app if script is executed directly
    main()








