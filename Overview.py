import streamlit as st

# Split Layout Welcome Section
col1, col2 = st.columns([1, 2])

with col1:
    st.image("images/Go_Auto.jpg", width=130)

with col2:
    st.markdown(
        """
        <div style="padding: 20px; text-align: left;">
            <h1 style="font-size: 36px; color: #4CAF50;">Welcome to Go Norquest!</h1>
            <p style="font-size: 18px; color: #555;">
            This project leverages cutting-edge data science and machine learning to provide actionable insights into vehicle sales trends. 
            Explore our data-driven strategies and AI-powered tools to optimize dealership performance.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )
