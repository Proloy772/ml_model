import streamlit as st
import pandas as pd
import joblib

# Load model
data = joblib.load("model.pkl")

model = data["model"]
features = data["features"]

st.title("🏠 House Price Prediction")

st.write("Enter house details")

BHK = st.number_input("BHK", min_value=1, value=2)

Area_sqft = st.number_input(
    "Area (sq ft)",
    min_value=100,
    value=1000
)

Bedrooms = st.number_input(
    "Bedrooms",
    min_value=1,
    value=2
)

Bathrooms = st.number_input(
    "Bathrooms",
    min_value=1,
    value=2
)

Floor = st.number_input(
    "Floor",
    min_value=0,
    value=1
)

Total_Floors = st.number_input(
    "Total Floors",
    min_value=1,
    value=5
)

Property_Age = st.number_input(
    "Property Age",
    min_value=0,
    value=5
)

Parking = st.number_input(
    "Parking",
    min_value=0,
    value=1
)

Balcony = st.number_input(
    "Balcony",
    min_value=0,
    value=1
)

Distance_to_City_Center_km = st.number_input(
    "Distance to City Center (km)",
    min_value=0.0,
    value=5.0
)

Price_per_sqft = st.number_input(
    "Price per sqft",
    min_value=0.0,
    value=5000.0
)

if st.button("Predict Price"):

    input_data = pd.DataFrame({
        "BHK": [BHK],
        "Area_sqft": [Area_sqft],
        "Bedrooms": [Bedrooms],
        "Bathrooms": [Bathrooms],
        "Floor": [Floor],
        "Total_Floors": [Total_Floors],
        "Property_Age": [Property_Age],
        "Parking": [Parking],
        "Balcony": [Balcony],
        "Distance_to_City_Center_km": [Distance_to_City_Center_km],
        "Price_per_sqft": [Price_per_sqft]
    })

    input_data = input_data[features]

    prediction = model.predict(input_data)

    st.success(
        f"Predicted House Price: ₹{prediction[0]:,.2f}"
    )