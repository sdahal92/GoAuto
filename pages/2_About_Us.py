import streamlit as st

# Set page configuration
st.set_page_config(page_title="Team Regression Rebels", layout="centered")

# Custom HTML for stylish topic header
st.markdown("""
    <style>
    .team-header {
        font-family: 'Arial', sans-serif;
        color: #5C4033; /* Rich brown text */
        background-color: #FFDAB9; /* Light peach background */
        padding: 20px;
        border-radius: 10px;
        text-align: center;
        box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.1);
    }
    </style>
    <div class="team-header">
        <h1>Team Regression Rebels</h1>
    </div>
""", unsafe_allow_html=True)
 st.image("images/Go_Auto.jpg", width=200)
