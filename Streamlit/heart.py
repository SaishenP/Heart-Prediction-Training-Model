import joblib
import numpy as np
import streamlit as st
import os

# Check Python and library versions
import sys
print("Python version:", sys.version)
print("Joblib version:", joblib.__version__)

# Check if the model file exists
model_path = 'heart.joblib'
if not os.path.exists(model_path):
    raise FileNotFoundError(f"Model file not found: {model_path}")

# Load the machine learning model
try:
    loaded_model = joblib.load(model_path)
except Exception as e:
    raise RuntimeError(f"Error loading the model: {str(e)}")

# Create a function for prediction
def heart_disease_prediction(input_data):
    try:
        # Convert input data to numeric values
        input_data_numeric = [float(x) for x in input_data]

        # Convert input data to numpy array
        input_data_as_numpy_array = np.asarray(input_data_numeric)

        # Reshape the array for prediction (one instance)
        input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)

        # Make prediction
        prediction = loaded_model.predict(input_data_reshaped)

        if prediction[0] == 0:
            return 'The person does not have heart disease'
        else:
            return 'The person does have heart disease'
    except Exception as e:
        return str(e)

def main():
    # Set page title and favicon
    st.set_page_config(page_title="Heart Disease Prediction", page_icon=":heart:")

    # Header/title of the app
    st.title('Heart Disease Prediction Web App')

    # Description of the app
    st.write("This application predicts the likelihood of heart disease based on various factors.")

    # Sliders for input factors
    age = st.slider('Age', min_value=20, max_value=100, step=1)
    sex = st.radio('Sex', ['Male', 'Female'])
    cp = st.selectbox('Chest Pain Type', [0, 1, 2, 3])
    trestbps = st.slider('Resting Blood Pressure (mm Hg)', min_value=80, max_value=200, step=1)
    chol = st.slider('Serum Cholesterol (mg/dl)', min_value=100, max_value=500, step=1)
    fbs = st.radio('Fasting Blood Sugar', ['<= 120 mg/dl', '> 120 mg/dl'])
    restecg = st.selectbox('Resting Electrocardiographic Results', [0, 1, 2])
    thalach = st.slider('Maximum Heart Rate (bpm)', min_value=50, max_value=200, step=1)
    exang = st.radio('Exercise Induced Angina', ['Yes', 'No'])
    oldpeak = st.slider('ST Depression induced by Exercise', min_value=0.0, max_value=10.0, step=0.1)
    slope = st.selectbox('Slope of the Peak Exercise ST Segment', [0, 1, 2])
    ca = st.select_slider('Number of Major Vessels Colored by Fluoroscopy', options=[0, 1, 2, 3])
    thal = st.select_slider('Thalassemia', options=[1, 2, 3])

    # Code for prediction
    if st.button('Predict'):
        input_data = [
            age,
            1 if sex == 'Male' else 0,
            cp,
            trestbps,
            chol,
            1 if fbs == '> 120 mg/dl' else 0,
            restecg,
            thalach,
            1 if exang == 'Yes' else 0,
            oldpeak,
            slope,
            ca,
            thal
        ]
        diagnosis = heart_disease_prediction(input_data)
        st.success(diagnosis)

if __name__ == "__main__":
    main()
