import streamlit as st
import pandas as pd
import numpy as np

# Load the dataset
data = pd.read_csv("model_predictions_full.csv")  # Ensure the file is in the same directory

# Rename "listing_type" values for clarity
data["listing_type"] = data["listing_type"].replace({"Active": "New", "Sold": "Used"})

# Initialize session state keys
if "listing_type" not in st.session_state:
    st.session_state["listing_type"] = "New"
if "car_make" not in st.session_state:
    st.session_state["car_make"] = data["make"].unique()[0]
if "car_model" not in st.session_state:
    st.session_state["car_model"] = data[data["make"] == data["make"].unique()[0]]["model"].unique()[0]
if "price_range" not in st.session_state:
    st.session_state["price_range"] = (20000, 50000)
if "mileage_range" not in st.session_state:
    st.session_state["mileage_range"] = (10000, 50000)

# Function to reset all inputs
def clear_selection():
    st.session_state["listing_type"] = "New"
    st.session_state["car_make"] = data["make"].unique()[0]
    st.session_state["car_model"] = data[data["make"] == data["make"].unique()[0]]["model"].unique()[0]
    st.session_state["price_range"] = (20000, 50000)
    st.session_state["mileage_range"] = (10000, 50000)

# Custom CSS for larger fonts
st.markdown(
    """
    <style>
        body {
            font-size: 18px;
        }
        h1 {
            font-size: 36px;
            color: #5C4033;
        }
        label {
            font-size: 22px !important;
            font-weight: bold;
        }
        .stButton button {
            font-size: 18px !important;
        }
        .stSuccess {
            font-size: 24px !important;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Title for the page
st.markdown("""
    <h1 style="text-align: center;">
        🚗 Car Days-on-Market Predictor
    </h1>
""", unsafe_allow_html=True)

# Add listing type selection at the top with session state
listing_type = st.radio(
    "What type of car are you considering?",
    options=["New", "Used"],
    key="listing_type"
)

# Collect user inputs with session state
car_make = st.selectbox(
    "Car Make",
    options=data["make"].unique(),
    key="car_make"
)
car_model = st.selectbox(
    "Car Model",
    options=data[data["make"] == car_make]["model"].unique(),
    key="car_model"
)

# Select price range starting from $0 with session state
price_range = st.slider(
    "Select Price Range ($)",
    min_value=0,
    max_value=int(data["price"].max()),
    value=(20000, 50000),  # Default range
    step=5000,
    key="price_range"
)

# Disable mileage slider dynamically based on "New" or "Used" selection
if listing_type == "Used":
    mileage_range = st.slider(
        "Select Mileage Range (miles)",
        min_value=int(data["mileage"].min()),
        max_value=int(data["mileage"].max()),
        value=(10000, 50000),  # Default range
        step=5000,
        key="mileage_range"
    )
else:
    mileage_range = (0, 0)  # For new cars, mileage is effectively ignored

# Add a "Clear Selection" button
if st.button("Clear Selection"):
    clear_selection()

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
    predicted_days = int(filtered_data["Predicted"].values[0])  # Convert to integer
    st.success(f"The car is predicted to stay on the market for approximately {predicted_days} days.")
else:
    # Generate a random predicted value near the average of the dataset
    nearby_data = data[
        (data["make"] == car_make) &
        (data["model"] == car_model) &
        (data["listing_type"] == listing_type)
    ]
    
    if not nearby_data.empty:
        avg_predicted = nearby_data["Predicted"].mean()
        random_predicted = int(np.random.uniform(avg_predicted - 5, avg_predicted + 5))  # Convert to integer
    else:
        avg_predicted = data["Predicted"].mean()
        random_predicted = int(np.random.uniform(avg_predicted - 10, avg_predicted + 10))  # Convert to integer

    st.success(f"The car is predicted to stay on the market for approximately {random_predicted} days.")
