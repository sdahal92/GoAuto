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
        <h1 style="font-size: 40px; font-weight: bold; margin-bottom: 10px;">Overview of the Project</h1>
        <p style="font-size: 22px; margin: 0;"> <!-- Increased font size -->
        This project was done as a part of the 3830 course in partnership with GoAuto to analyze Go Auto’s vehicle sales data using a dataset from the Canadian Black Book (CBB).
        </p>
    </div>
    """,
    unsafe_allow_html=True,
)

# Project Details Section
st.markdown(
    """
    <div style="text-align: justify; font-size: 30px; color: #555; margin-top: 20px;"> <!-- Increased font size -->
        <p>The dataset includes:</p>
        <ul>
            <li style="font-size: 22px"><b style="font-size: 22px">Vehicle details:</b> year, make, model, mileage, and price.</li>
            <li style="font-size: 22px"><b style="font-size: 22px">Dealership information:</b> location and listing specifics.</li>
            <li style="font-size: 22px"><b style="font-size: 22px">Vehicle listings:</b> Active and sold vehicles from Edmonton dealerships within the last 30 days.</li>
        </ul>
    </div>
    """,
    unsafe_allow_html=True,
)

