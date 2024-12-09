import streamlit as st

# Set page configuration
st.set_page_config(page_title="Team Regression Rebels", layout="centered")

# Custom HTML for "Meet Our Team" and "Team Regression Rebels"
st.markdown("""
    <style>
    .meet-team {
        font-family: 'Arial', sans-serif;
        color: #4A4A4A; /* Dark gray text */
        text-align: center;
        font-size: 60px; /* Large font size */
        font-weight: bold; /* Bold text */
        margin-bottom: 30px;
        margin-top: 20px;
        line-height: 1.2;
    }
    .team-header {
        font-family: 'Arial', sans-serif;
        color: #FF0000; /* Red text */
        background: linear-gradient(to right, #FFEFBA, #FFFFFF); /* Soft peach gradient */
        padding: 20px;
        border-radius: 15px;
        text-align: center;
        box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.2);
        font-size: 50px; /* Consistent header font size */
        font-weight: bold;
        line-height: 1.2;
    }
    .spacer {
        margin-top: 40px; /* Adds vertical space */
    }
    .roles {
        font-family: 'Arial', sans-serif;
        color: #4A4A4A; /* Dark gray text */
        text-align: center;
        font-size: 20px; /* Font size for roles */
        margin-top: 20px;
        line-height: 1.5;
    }
    </style>
    <div class="meet-team">
        <p>Meet Our Team</p>
    </div>
    <div class="team-header">
        <h1>Team</h1>
        <h1>Regression Rebels</h1>
    </div>
    <div class="spacer"></div>
""", unsafe_allow_html=True)

# Add the team photo
st.image("images/Screenshot 2024-12-08 194954.png", width=900)

# Add roles below the photo
st.markdown("""
    <div class="roles">
        <p><strong>Rohit:</strong> Data Preprocessing Lead</p>
        <p><strong>Spandan Dahal:</strong> Model Developer</p>
        <p><strong>Abhinav Datt:</strong> Visualization Expert</p>
        <p><strong>Jatin Dadhyan:</strong> Project Coordinator</p>
    </div>
""", unsafe_allow_html=True)
