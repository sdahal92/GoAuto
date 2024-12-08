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
        <p style="font-size: 18px; margin: 0;">
        Analyzing Go Auto’s vehicle sales data, sourced from the Canadian Black Book (CBB), to uncover trends, optimize pricing strategies, and enhance dealership performance.
        </p>
    </div>
    """,
    unsafe_allow_html=True,
)

# Project Details Section
st.markdown(
    """
    <div style="text-align: justify; font-size: 16px; color: #555; margin-top: 20px;">
        <p>The dataset includes:</p>
        <ul>
            <li><b>Vehicle details:</b> year, make, model, mileage, and price.</li>
            <li><b>Dealership information:</b> location and listing specifics.</li>
            <li><b>Vehicle listings:</b> Active and sold vehicles from Edmonton dealerships within the last 30 days.</li>
        </ul>
    </div>
    """,
    unsafe_allow_html=True,
)

# Project Highlights Section
st.markdown("### Project Highlights")  # Section Title

# Highlight Text in Columns (No Images)
highlight_col1, highlight_col2, highlight_col3 = st.columns(3)

with highlight_col1:
    st.markdown(
        "<p style='text-align: center; font-size: 18px;'>Deep insights into sales trends.</p>", 
        unsafe_allow_html=True
    )

with highlight_col2:
    st.markdown(
        "<p style='text-align: center; font-size: 18px;'>AI-powered predictions.</p>", 
        unsafe_allow_html=True
    )

with highlight_col3:
    st.markdown(
        "<p style='text-align: center; font-size: 18px;'>Customer preference analysis.</p>", 
        unsafe_allow_html=True
    )
