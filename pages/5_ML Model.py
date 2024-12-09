import streamlit as st
import pandas as pd

# Load the dataset
data = pd.read_csv("model_predictions_full.csv")  # Ensure the file is in the same directory

# Rename "listing_type" values for clarity
data["listing_type"] = data["listing_type"].replace({"Active": "New", "Sold": "Used"})

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

# Select price range
price_range = st.slider(
    "Select Price Range ($)",
    min_value=int(data["price"].min()),
    max_value=int(data["price"].max()),
    value=(20000, 50000),  # Default range
    step=5000
)

# Select mileage range
mileage_range = st.slider(
    "Select Mileage Range (miles)",
    min_value=int(data["mileage"].min()),
    max_value=int(data["mileage"].max()),
    value=(10000, 50000),  # Default range
    step=5000
)

listing_type = st.radio("What type of car are you considering?", options=["New", "Used"])

# Filter the dataset based on inputs
filtered_data = data[
    (data["make"] == car_make) &
    (data["model"] == car_model) &
    (data["price"] >= price_range[0]) & (data["price"] <= price_range[1]) &
    (data["mileage"] >= mileage_range[0]) & (data["mileage"] <= mileage_range[1]) &
    (data["listing_type"] == listing_type)
]

# Display the predicted days on market
if not filtered_data.empty:
    predicted_days = filtered_data["Predicted"].values[0]  # Replace "Predicted" if the column name is different
    st.success(f"The car is predicted to stay on the market for approximately {round(predicted_days, 2)} days.")
else:
    st.error("No matching car found in the dataset. Please adjust the inputs.")
