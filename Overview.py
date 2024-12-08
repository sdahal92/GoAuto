import streamlit as st

# Header with Images in Top-Left and Top-Right Corners
col1, col2, col3 = st.columns([1, 2, 1])  # Adjust column widths as needed

with col1:
    st.image("images/Go_Auto.jpg", width=130)  # Adjust width for smaller size

with col2:
    st.markdown("<div></div>", unsafe_allow_html=True)  # Empty column for spacing

with col3:
    st.image("images/Norquest Logo.jpeg", width=130)  # Adjust width for smaller size

# Vibrant Full-Width Banner with Project Overview
st.markdown(
    """
    <div style="
        padding: 30px; 
        text-align: center; 
        background: linear-gradient(to right, #ff7e5f, #feb47b); 
        color: white; 
        border-radius: 5px;">
        <h1 style="font-size: 30px; font-weight: bold; margin-bottom: 20px;">Overview of the Project</h1>
        <p style="font-size: 24px; margin: 0;"> 
        This project was done as a part of the 3830 course in partnership with GoAuto to analyze Go Auto’s vehicle sales data using a dataset from the Canadian Black Book (CBB).
        </p>
    </div>
    """,
    unsafe_allow_html=True,
)

# Objective Section
st.markdown(
    """
    <div style="text-align: justify; font-size: 30px; color: #555; margin-top: 30px;">
        <p><b>Objective:</b> Predict the 'Days on Market' for vehicles listed by Go Auto.</p>
        <p>This project was divided into three major parts:</p>
        <ol style="font-size: 30px;">
            <li><b>Exploratory Data Analysis (EDA):</b> Analyzed the dataset to understand trends, patterns, and key features.</li>
            <li><b>Machine Learning Model:</b> Built a regression model to predict the number of days a vehicle will take to sell.</li>
            <li><b>App Development:</b> Developed this app to visualize the results and insights interactively.</li>
        </ol>
    </div>
    """,
    unsafe_allow_html=True,
)

# Project Details Section
st.markdown(
    """
    <div style="text-align: justify; font-size: 30px; color: #555; margin-top: 30px;"> 
        <p><b>The dataset includes:</b></p>
        <ul style="font-size: 30px; margin-top: 20px;">
            <li><b>Vehicle details:</b> year, make, model, mileage, and price.</li>
            <li><b>Dealership information:</b> location and listing specifics.</li>
            <li><b>Vehicle listings:</b> Active and sold vehicles from Edmonton dealerships within the last 30 days.</li>
        </ul>
    </div>
    """,
    unsafe_allow_html=True,
)

# Project Highlights Section
st.markdown(
    """
    <div style="text-align: center; font-size: 30px; color: #555; margin-top: 30px;">
        <p><b>Project Highlights:</b></p>
        <ul style="font-size: 30px; margin-top: 20px; text-align: left;">
            <li>Gained deep insights into vehicle sales trends.</li>
            <li>Developed AI-powered predictions for days on market.</li>
            <li>Provided actionable recommendations for pricing strategies.</li>
            <li>Enhanced understanding of customer preferences.</li>
        </ul>
    </div>
    """,
    unsafe_allow_html=True,
)
