import streamlit as st
import pandas as pd

# Load the dataset
data = pd.read_csv("model_predictions_full.csv")  # Ensure the file is in the same directory as this script

# Title for the page
st.markdown("""
    <h1 style="text-align: center; color: #5C4033;">
        🚗 Car Days-on-Market Predictor
    </h1>
""", unsafe_allow_html=True)

st.markdown("### Enter Car Details")

# Collect user inputs
car_make = st.selectbox("Car Make", options=data["make"].unique())
car_model = st.selectbox("Car Model", options=data[data["make"] == car_make]["model"].unique())
price = st.slider("Car Price ($)", min_value=int(data["price"].min()), max_value=int(data["price"].max()), step=5000, value=30000)
mileage = st.slider("Car Mileage (miles)", min_value=int(data["mileage"].min()), max_value=int(data["mileage"].max()), step=5000, value=50000)
listing_type = st.radio("Listing Type", options=["Active", "Sold"])

# Filter the dataset based on user inputs
filtered_data = data[
    (data["make"] == car_make) &
    (data["model"] == car_model) &
    (data["price"] >= price - 5000) & (data["price"] <= price + 5000) &
    (data["mileage"] >= mileage - 5000) & (data["mileage"] <= mileage + 5000) &
    (data["listing_type"].str.lower() == listing_type.lower())  # Match listing type
]

# Display the predicted days on market
if not filtered_data.empty:
    predicted_days = filtered_data["Predicted"].values[0]  # Replace "Predicted" if the column name is different
    st.success(f"The car is predicted to stay on the market for approximately {round(predicted_days, 2)} days.")
else:
    st.error("No matching car found in the dataset. Please adjust the inputs.")
