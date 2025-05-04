# importing the libaries

import numpy as np
import pickle # to load the model
import streamlit as st
import pandas as pd
import requests


# Loading the saved model copy the loaded_model line of code from jupyter notebook
# copy the path to where the loaded model is savel
# change the \ to /
#loaded_model = pickle.load(open('E:\Ezekiel\Model_Deployment/trained_model1.sav', 'rb'))
#loaded_model = pickle.load(open('https://github.com/ezekielmose/Machine-Learning/blob/main/trained_model1.sav', 'rb')) 

#import pickle


# URL of the .sav file
url = 'https://raw.githubusercontent.com/Wisaji/Heart_Disease_ModelDeployment/refs/heads/main/hd_trained_model.sav'

# Download the file
loaded_model1 = requests.get(url)

# Save the downloaded content to a temporary file
with open('hd_trained_model.sav', 'wb') as f:
    f.write(loaded_model1.content)

# Load the saved model
with open('hd_trained_model.sav', 'rb') as f:
    loaded_model1 = pickle.load(f)

# Now, you can use the loaded model for predictions


# creating a function for prediction
def hearth_disease_prediction(input_data):

    ## Copy from Jupyter, the code for the unstandadized data 
    ## changing input data to numpy array because processing is easier than list 
    input_data_as_numpy_array= np.array(input_data)
    # reshaping the array for predicting 
    
    # Prepare the input data as an array or DataFrame (depending on your model)
    # input_data = [age, sex, Chest_Pain, Blood_Pressure]
    input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)


   #  input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)
    prediction = loaded_model1.predict(input_data_reshaped)
    
    # print(prediction)
    if prediction [0] == 0:
        return "The Person has Heart Disease" # insted of print change to return
    else:
        return "The Person Does not have a Heart Disease" # insted of print change to return  
    
# Streamlit library to craete a user interface
def main():
    
    # Interface title
    st.title("Heart Disease Prediction Machine Learning Model ")
    
    #getting the input data from the user  
    age = st.text_input("Enter the Patient's Age 15 - 80")
    #sex = st.text_input("Enter the Patient's Gender (0 [F] or 1[M])")

    # DROPDOWN DRROP BOX
    sex = st.selectbox( "What is the Gender", options=["Female", "Male"] )
    # Map the selected gender string to numeric value if needed
    gender_value = 0 if sex == "Female" else 1

    
    Chest_Pain = st.text_input("Chest Pain level (0,1,2 or 3)")
    Blood_Pressure= st.text_input("The Blood Pressure(mm Hg)level (94-200) ")
    cholestoral = st.text_input("Cholestoral Level (mg/dl) (131 -290)")
    Fasting_Blood_Sugar = st.text_input("Patient's Fasting Blood Sugar (0,1)")
    resting_electrocardiographic = st.text_input("Electrocardiographic level (0, 1 or 2)")
    Maximum_Heart_Rate= st.text_input("Maximum Heart Rate (99 - 162)")
    Excersize_Includes = st.text_input("Enter the Patient's Excersize_Includes")
    ST_Depression = st.text_input("Patient's ST Depression [ECG or EKG] (0.0 - 4.4)")
    Slope_of_Excersize	 = st.text_input("Patient's Slope of Excersize (0,1 or 2)")
    Number_of_vessels = st.text_input("Number of vessels (0, 1,2,3 or 4)")
    #Thalassemia = st.text_input("Thalassemia (0, 1,2,3 or 4)")
    #INCREMENT/DECREAMENT OPTIONS
    Thalassemia = st.number_input( "Thalassemia Level", 
        min_value=1, 
        max_value=4, 
        step=2)
    
    
    ## Numeric conversion
    # Convert inputs to numeric using pd.to_numeric or float conversion
    age = pd.to_numeric(age, errors='coerce')
    sex = pd.to_numeric(sex, errors='coerce')
    Chest_Pain = pd.to_numeric(Chest_Pain, errors='coerce')
    Blood_Pressure = pd.to_numeric(Blood_Pressure, errors='coerce')
    cholestoral = pd.to_numeric(cholestoral, errors='coerce')
    Fasting_Blood_Sugar = pd.to_numeric(Fasting_Blood_Sugar, errors='coerce')
    resting_electrocardiographic = pd.to_numeric(resting_electrocardiographic, errors='coerce')
    Maximum_Heart_Rate = pd.to_numeric(Maximum_Heart_Rate, errors='coerce')
    Excersize_Includes = pd.to_numeric(Excersize_Includes, errors='coerce')
    ST_Depression = pd.to_numeric(ST_Depression, errors='coerce')
    Slope_of_Excersize = pd.to_numeric(Slope_of_Excersize, errors='coerce')
    Number_of_vessels = pd.to_numeric(Number_of_vessels, errors='coerce')
    Thalassemia = pd.to_numeric(Thalassemia, errors='coerce')

    # code for prediction
    diagnosis = '' # string tha ontaons null values whose values are stored in the prediction
    
    # creating  a prediction button
    if st.button("PREDICT"):
        diagnosis = hearth_disease_prediction([age,gender_value,Chest_Pain,Blood_Pressure,cholestoral,Fasting_Blood_Sugar, resting_electrocardiographic,Maximum_Heart_Rate,Excersize_Includes,ST_Depression,Slope_of_Excersize,Number_of_vessels,Thalassemia])
    st.success(diagnosis)
    
 
# this is to allow our web app to run from anaconda command prompt where the cmd takes the main() only and runs the code
if __name__ == '__main__':
    main()
    

    
    
    
    
    
    
    
    
    
    
    
    
