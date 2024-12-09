import streamlit as st

# Set page configuration
st.set_page_config(page_title="Team Regression Rebels", layout="centered")

# Custom HTML for the header and centered photo
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
    .team-container {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        height: 80vh; /* Adjust to vertically center */
    }
    .team-member img {
        width: auto; /* Maintain original width */
        max-width: 80%; /* Ensure the image scales responsively */
        height: auto; /* Maintain aspect ratio */
        box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.2);
    }
    .team-member h3 {
        font-family: 'Arial', sans-serif;
        color: #4A4A4A;
        margin-top: 10px;
        text-align: center;
    }
    </style>
    <div class="team-header">
        <h1>Team Regression Rebels</h1>
    </div>
    <div class="team-container">
        <div class="team-member">
            <img src="images/Screenshot 2024-12-08 194954.png" alt="Team Member">
            <h3>John Doe</h3>
        </div>
    </div>
""", unsafe_allow_html=True)
