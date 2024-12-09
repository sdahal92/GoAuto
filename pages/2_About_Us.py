import streamlit as st

# Set page configuration
st.set_page_config(page_title="Team Regression Rebels", layout="centered")

# Custom HTML for the header
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
    .team-member {
        text-align: center;
        margin-top: 30px;
    }
    .team-member img {
        border-radius: 50%;
        width: 200px;
        height: 200px;
        box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.2);
    }
    .team-member h3 {
        font-family: 'Arial', sans-serif;
        color: #4A4A4A;
        margin-top: 10px;
    }
    </style>
    <div class="team-header">
        <h1>Team Regression Rebels</h1>
    </div>
""", unsafe_allow_html=True)

# Add the photo and name
st.markdown("""
        <img src="images/Screenshot 2024-12-08 194954.png" alt="Team Member">
   
    </div>
""", unsafe_allow_html=True)
