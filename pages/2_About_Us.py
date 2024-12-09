import streamlit as st

# Set page configuration
st.set_page_config(page_title="Team Regression Rebels", layout="centered")

# Custom HTML for stylish header with gradient background
st.markdown("""
    <style>
    .team-header {
        font-family: 'Arial', sans-serif;
        color: #FF0000; /* Red text */
        background: linear-gradient(to right, #FFEFBA, #FFFFFF); /* Soft peach gradient */
        padding: 20px;
        border-radius: 15px;
        text-align: center;
        box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.2);
        line-height: 1.5; /* Adjust line spacing */
    }
    .spacer {
        margin-top: 40px; /* Adds vertical space */
    }
    </style>
    <div class="team-header">
        <h1> Team Regression Rebels</h1>
    </div>
    <div class="spacer"></div> <!-- Gap between title and photo -->
""", unsafe_allow_html=True)

# Add the photo with appropriate size
st.image("images/Screenshot 2024-12-08 194954.png", width=900)
