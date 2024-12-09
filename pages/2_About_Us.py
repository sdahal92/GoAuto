import streamlit as st

# Set page configuration
st.set_page_config(page_title="About Us - Regression Rebels", layout="centered")

# Custom HTML for stylish heading with peach background and refined text
st.markdown("""
    <style>
    .team-header {
        font-family: 'Arial', sans-serif;
        color: #5C4033; /* Rich brown for text */
        background-color: #FFDAB9; /* Light peach background */
        padding: 20px;
        border-radius: 10px;
        text-align: center;
        box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.1);
    }
    .main-text {
        font-family: 'Georgia', serif;
        color: #4A4A4A; /* Dark gray for body text */
        line-height: 1.6;
        font-size: 16px;
    }
    </style>
    <div class="team-header">
        <h1>Team Regression Rebels</h1>
        <p>Innovators in Machine Learning and Predictive Analytics</p>
    </div>
    <div class="main-text">
        Welcome to the <strong>Regression Rebels</strong> team page! We are a group of enthusiastic machine learning practitioners dedicated to creating impactful solutions. 
        <br><br>
        Our mission is to leverage the power of data to drive innovation and deliver outstanding results. Together, we bring expertise in predictive modeling, data analysis, and cutting-edge AI to tackle real-world challenges with precision and creativity.
    </div>
""", unsafe_allow_html=True)
