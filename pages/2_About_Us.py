import streamlit as st
streamlit run team_page.py

# Set page configuration
st.set_page_config(page_title="Team Regression Rebels", layout="centered")

# Custom HTML for "Meet Our Team" and "Team Regression Rebels" with fixed styles
st.markdown("""
    <style>
    /* Styling for "Meet Our Team" */
    .meet-team {
        font-family: 'Arial', sans-serif;
        color: #4A4A4A; /* Dark gray text */
        text-align: center;
        font-size: 80px; /* Large font size */
        font-weight: bold; /* Bold text */
        margin-bottom: 30px;
        margin-top: 20px;
        line-height: 1.2;
    }
    /* Styling for "Team Regression Rebels" */
    .team-header {
        font-family: 'Arial', sans-serif;
        color: #FF0000; /* Red text */
        background: linear-gradient(to right, #FFEFBA, #FFFFFF); /* Soft peach gradient */
        padding: 20px;
        border-radius: 15px;
        text-align: center;
        box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.2);
        font-size: 70px !important; /* Enforced font size */
        font-weight: bold; /* Bold text */
        line-height: 1.2;
    }
    /* Override Streamlit's internal styles to prevent resizing */
    html, body, [class*="css"] {
        font-size: 16px !important; /* Base font size for all elements */
    }
    </style>
    <div class="meet-team">
        <p>Meet Our Team</p>
    </div>
    <div class="team-header">
        <h1 style="margin: 0;">Team</h1>
        <h1 style="margin: 0;">Regression Rebels</h1>
    </div>
""", unsafe_allow_html=True)
