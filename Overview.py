import streamlit as st

# Card Style Welcome Section
st.markdown(
    """
    <div style="
        text-align: center; 
        margin-top: -20px; 
        padding: 20px; 
        background-color: #ffffff; 
        border-radius: 15px; 
        box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.2);">
        <h1 style="font-size: 36px; color: #4CAF50; margin-bottom: 10px;">Welcome to Go Norquest!</h1>
        <p style="font-size: 18px; color: #555;">
        This project leverages cutting-edge data science and machine learning to provide actionable insights into vehicle sales trends. 
        Explore our data-driven strategies and AI-powered tools to optimize dealership performance.
        </p>
    </div>
    """,
    unsafe_allow_html=True,
)
