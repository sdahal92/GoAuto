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
    </style>
    <div class="team-header">
        <h1>Team Regression Rebels</h1>
    </div>
""", unsafe_allow_html=True)

# Add the team member's photo
st.markdown("<h2 style='text-align: center;'>Meet Our Team</h2>", unsafe_allow_html=True)

# Display the image
st.image("images/Screenshot 2024-12-08 194954.png", caption="John Doe - Team Member", width=900)
