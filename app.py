import streamlit as st
import pandas as pd
import joblib

# Load the trained model
model = joblib.load('https://raw.githubusercontent.com/meshachaderele/timber-price/main/pipeline_model.joblib')


def predict_price(features):
    # Convert input dictionary to DataFrame
    input_data = pd.DataFrame([features])
    # Make prediction
    prediction = model.predict(input_data)
    return prediction[0]


def main():
    st.title('Timber Price Prediction App')
    st.write('Enter the following details to predict Timber Price:')

    # Input fields
    dbh = st.number_input('Diameter at Breast Height (DBH)', min_value=0.1, step=0.1)
    height = st.number_input('Height (in feet)', min_value=1.0, step=1.0)
    age = st.number_input('Age (in years)', min_value=1, step=1)
    species = st.selectbox('Species', ['Pine', 'Oak', 'Maple', 'Spruce'])
    soil_type = st.selectbox('Soil Type', ['Sandy', 'Clay', 'Loam'])
    latitude = st.number_input('Latitude', min_value=-90.0, max_value=90.0, step=0.001)
    longitude = st.number_input('Longitude', min_value=-180.0, max_value=180.0, step=0.001)

    # Create a dictionary from user inputs
    features = {
        'DBH': dbh,
        'Height': height,
        'Age': age,
        'Species': species,
        'Soil_Type': soil_type,
        'Latitude': latitude,
        'Longitude': longitude
    }

    # Predict Timber Price
    if st.button('Predict'):
        prediction = predict_price(features)
        st.success(f'Predicted Timber Price: ${prediction:.2f}')


if __name__ == '__main__':
    main()
