import streamlit as st

# Icon + Welcome Text Section
st.markdown(
    """
    <div style="text-align: center; margin-top: -20px;">
        <img src="https://via.placeholder.com/80" alt="Icon" style="width: 80px; margin-bottom: 10px;">
        <h1 style="font-size: 36px; font-weight: bold; color: #4CAF50; margin: 0;">Welcome to Go Norquest!</h1>
        <p style="font-size: 18px; color: #555; margin-top: 10px;">
        This project leverages cutting-edge data science and machine learning to provide actionable insights into vehicle sales trends.
        </p>
    </div>
    """,
    unsafe_allow_html=True,
)
