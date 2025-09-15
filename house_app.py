import streamlit as st
import joblib
import numpy as np

# Load trained model
model = joblib.load("house_price_model_simple.pkl")

st.title("🏡 House Price Prediction App")

st.write("Fill in the details and click *Predict* to see the estimated price.")

# Input fields
overallqual = st.number_input("Overall Quality (1-10)", min_value=1, max_value=10, value=5)
grlivarea = st.number_input("Above Ground Living Area (sq ft)", min_value=500, max_value=5000, value=1500)
garagecars = st.number_input("Garage Cars", min_value=0, max_value=5, value=2)
totalbsmt = st.number_input("Total Basement Area (sq ft)", min_value=0, max_value=3000, value=800)
fullbath = st.number_input("Number of Full Bathrooms", min_value=0, max_value=5, value=2)

# Predict button
if st.button("Predict"):
    input_data = np.array([[overallqual, grlivarea, garagecars, totalbsmt, fullbath]])
    prediction = model.predict(input_data)[0]
    st.success(f"💰 Estimated House Price: ${prediction:,.0f}")