import pickle
import numpy as np
import streamlit as st

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
    fbs = st.radio('Fasting Blood Sugar (mg/dl)', ['<= 120 mg/dl', '> 120 mg/dl'])
    restecg = st.selectbox('Resting Electrocardiographic Results', [0, 1, 2])
    thalach = st.slider('Maximum Heart Rate (bpm)', min_value=50, max_value=200, step=1)
    exang = st.radio('Exercise Induced Angina', ['Yes', 'No'])
    oldpeak = st.slider('ST Depression induced by Exercise', min_value=0.0, max_value=10.0, step=0.1)
    slope = st.selectbox('Slope of the Peak Exercise ST Segment', [0, 1, 2])
    ca = st.select_slider('Number of Major Vessels Colored by Fluoroscopy', options=[0, 1, 2, 3])
    thal = st.select_slider('Thalassemia', options=[1, 2, 3])

if __name__ == "__main__":
    main()