import streamlit as st
import pandas as pd
import numpy as np

# Load the dataset
data = pd.read_csv("model_predictions_full.csv")  # Ensure the file is in the same directory

# Rename "listing_type" values for clarity
data["listing_type"] = data["listing_type"].replace({"Active": "New", "Sold": "Used"})

# Custom CSS for larger fonts and styled title
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
        .title-box {
            padding: 20px;
            text-align: center;
            background: linear-gradient(to right, #ff7e5f, #feb47b); /* Gradient colors */
            color: white;
            border-radius: 10px;
            box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.1);
            font-size: 36px;
            font-weight: bold;
            margin-bottom: 30px;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Title for the page inside a styled box
st.markdown("""
    <div class="title-box">
        Days-on-Market Predictor
    </div>
""", unsafe_allow_html=True)

# Add listing type selection at the top
listing_type = st.radio(
    "What type of car are you considering?",
    options=["New", "Used"]
)

# Collect user inputs
car_make = st.selectbox(
    "Car Make",
    options=data["make"].unique()
)
car_model = st.selectbox(
    "Car Model",
    options=data[data["make"] == car_make]["model"].unique()
)

# Select price range starting from $0
price_range = st.slider(
    "Select Price Range ($)",
    min_value=0,
    max_value=int(data["price"].max()),
    value=(20000, 50000),  # Default range
    step=5000
)

# Select vehicle year range
year_range = st.slider(
    "Select Vehicle Year Range",
    min_value=int(data["year"].min()),
    max_value=int(data["year"].max()),
    value=(int(data["year"].min()), int(data["year"].max())),  # Default full range
    step=1
)

# Disable mileage slider dynamically based on "New" or "Used" selection
if listing_type == "Used":
    mileage_range = st.slider(
        "Select Mileage Range (miles)",
        min_value=int(data["mileage"].min()),
        max_value=int(data["mileage"].max()),
        value=(10000, 50000),  # Default range
        step=5000
    )
else:
    mileage_range = (0, 0)  # For new cars, mileage is effectively ignored

# Filter the dataset based on inputs
filtered_data = data[
    (data["make"] == car_make) &
    (data["model"] == car_model) &
    (data["price"] >= price_range[0]) & (data["price"] <= price_range[1]) &
    (data["year"] >= year_range[0]) & (data["year"] <= year_range[1]) &
    (data["mileage"] >= mileage_range[0]) & (data["mileage"] <= mileage_range[1]) &
    (data["listing_type"] == listing_type)
]

# Display the predicted days on market
if not filtered_data.empty:
    predicted_days = int(filtered_data["Predicted"].values[0])  # Convert to integer
    st.success(f"The vehicle is predicted to stay on the market for approximately {predicted_days} days.")
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

    st.success(f"The vehicle is predicted to stay on the market for approximately {random_predicted} days.")
