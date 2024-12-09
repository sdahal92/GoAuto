import streamlit as st

# Set page configuration
st.set_page_config(page_title="About Us - Regression Rebels", layout="centered")

# Custom HTML for stylish heading
st.markdown("""
    <style>
    .team-header {
        font-family: 'Arial', sans-serif;
        color: #FFFFFF;
        background-color: #4CAF50;
        padding: 20px;
        border-radius: 10px;
        text-align: center;
        box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.3);
    }
    </style>
    <div class="team-header">
        <h1>Team Regression Rebels</h1>
        <p>Innovators in Machine Learning and Predictive Analytics</p>
    </div>
""", unsafe_allow_html=True)

# Add a description below the heading
st.write("""
Welcome to the **Regression Rebels** team page! We are a group of enthusiastic machine learning practitioners dedicated to creating impactful solutions. Our mission is to leverage the power of data to drive innovation and deliver outstanding results.
""")
