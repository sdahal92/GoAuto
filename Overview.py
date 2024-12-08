import streamlit as st

# Vibrant Full-Width Welcome Banner
st.markdown(
    """
    <div style="
        padding: 30px; 
        text-align: center; 
        background: linear-gradient(to right, #ff7e5f, #feb47b); 
        color: white; 
        border-radius: 5px;">
        <h1 style="font-size: 40px; font-weight: bold; margin-bottom: 10px;">Welcome to Go Norquest!</h1>
        <p style="font-size: 18px; margin: 0;">
        This project leverages cutting-edge data science and machine learning to provide actionable insights into vehicle sales trends.
        </p>
    </div>
    """,
    unsafe_allow_html=True,
)
