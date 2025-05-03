import streamlit as st
import requests

# Streamlit app title
st.title("Penguin Species Prediction")
st.subheader("Enter the penguin details below to predict the species.")

# Create a form for inputs
with st.form("penguin_form"):
    # Dropdown for categorical input: island
    island = st.selectbox("Select the Island", ['Biscoe', 'Torgersen', 'Dream'])
    
    # Numerical input fields
    bill_length_mm = st.number_input("Bill Length (mm)", min_value=0.0, step=0.1)
    bill_depth_mm = st.number_input("Bill Depth (mm)", min_value=0.0, step=0.1)
    flipper_length_mm = st.number_input("Flipper Length (mm)", min_value=0, step=1)
    body_mass_g = st.number_input("Body Mass (g)", min_value=0, step=1)
    
    # Dropdown for categorical input: sex
    sex = st.selectbox("Select the Sex", ['Male', 'Female'])
    
    # Submit button
    submitted = st.form_submit_button("Submit")

# Handle form submission
if submitted:
    # Prepare the input data for the backend API
    input_data = {
        "island": island,
        "bill_length_mm": bill_length_mm,
        "bill_depth_mm": bill_depth_mm,
        "flipper_length_mm": flipper_length_mm,
        "body_mass_g": body_mass_g,
        "sex": sex
    }
    
    # Call the backend API
    try:
        # Replace with your backend API URL
        backend_url = "http://127.0.0.1:5000/predict"
        response = requests.post(backend_url, json=input_data)
        
        if response.status_code == 200:
            prediction = response.json().get("species")
            st.success(f"Predicted Penguin Species:  '{prediction}'")
        else:
            st.error(f"Failed to get prediction: '{response.text}'")
    except Exception as e:
        st.error(f"Error connecting to backend: {str(e)}")
