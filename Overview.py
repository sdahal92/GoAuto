import streamlit as st

# Minimalistic Welcome Section
st.markdown(
    """
    <div style="text-align: center; margin-top: -10px;">
        <h1 style="font-size: 36px; font-weight: bold; color: #333; margin-bottom: 5px; text-decoration: underline;">
            Welcome to Go Norquest!
        </h1>
        <p style="font-size: 18px; color: #555;">
        This project leverages cutting-edge data science and machine learning to provide actionable insights into vehicle sales trends.
        </p>
    </div>
    """,
    unsafe_allow_html=True,
)
