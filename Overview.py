import streamlit as st

# Header with Images in Top-Left and Top-Right Corners
col1, col2, col3 = st.columns([1, 2, 1])  # Adjust column widths as needed

with col1:
    st.image("images/Go_Auto.jpg", width=200)  # Adjust width for smaller size

with col2:
    st.markdown("<div></div>", unsafe_allow_html=True)  # Empty column for spacing

with col3:
    st.image("images/Norquest Logo.jpeg", width=200)  # Adjust width for smaller size

# Vibrant Full-Width Banner with Project Overview
st.markdown(
    """
    <div style="
        padding: 30px; 
        text-align: center; 
        background: linear-gradient(to right, #ff7e5f, #feb47b); 
        color: white; 
        border-radius: 5px;">
        <h1 style="font-size: 40px; font-weight: bold; margin-bottom: 20px;">Overview of the Project</h1>
        <p style="font-size: 20px; margin: 0;"> 
        This project was done as a part of the 3830 course in partnership with GoAuto to analyze Go Auto’s vehicle sales data using a dataset from the Canadian Black Book (CBB).
        </p>
    </div>
    """,
    unsafe_allow_html=True,
)

# Project Details Section
st.markdown(
    """
    <div style="text-align: justify; font-size: 20px; color: #555; margin-top: 30px;"> 
        <p style="font-size: 20px;"><b>The dataset includes:</b></p>
        <ul style="font-size: 20px; margin-top: 20px;">
            <li style="font-size: 20px;"><b>Vehicle details:</b> year, make, model, mileage, and price.</li>
            <li style="font-size: 20px;"><b>Dealership information:</b> location and listing specifics.</li>
            <li style="font-size: 20px;"><b>Vehicle listings:</b> Active and sold vehicles from Edmonton dealerships within the last 30 days.</li>
        </ul>
    </div>
    """,
    unsafe_allow_html=True,
)

# Objective Section
st.markdown(
    """
    <div style="text-align: justify; font-size: 20px; color: #555; margin-top: 30px;">
        <p style="font-size: 20px;"><b>Objective:</b> Predict the 'Days on Market' for vehicles listed by Go Auto.</p>
        <p style="font-size: 20px;">This project was divided into three major parts:</p>
        <ol style="font-size: 20px; margin-top: 20px;">
            <li style="font-size: 20px;"><b>Exploratory Data Analysis (EDA):</b> Analyzed the dataset to understand trends, patterns, and key features.</li>
            <li style="font-size: 20px;"><b>Machine Learning Model:</b> Built a regression model to predict the number of days a vehicle will take to sell .Also,build visualizations using PowerBI.</li>
            <li style="font-size: 20px;"><b>App Development:</b> Developed this app to visualize the results and insights interactively.</li>
        </ol>
    </div>
    """,
    unsafe_allow_html=True,
)
