import streamlit as st

# Set page configuration
st.set_page_config(page_title="Team Regression Rebels", layout="centered")

# Custom HTML for "Team Regression Rebels" Header
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
        font-size: 50px; /* Consistent header font size */
        font-weight: bold;
        line-height: 1.2;
        margin-top: 30px;
    }
    .roles {
        font-family: 'Arial', sans-serif;
        color: #4A4A4A; /* Dark gray text */
        text-align: center;
        font-size: 18px; /* Font size for roles */
        line-height: 1.5;
        margin-top: 20px;
    }
    </style>
    <div class="team-header">
        <h1>Team</h1>
        <h1>Regression Rebels</h1>
    </div>
""", unsafe_allow_html=True)

# Add the team photo
st.image("images/Screenshot 2024-12-08 194954.png", width=900)

# Display roles in columns
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown("""
    <div class="roles">
        <p><strong>Rohit</strong></p>
        <p>Data Preprocessing Lead</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="roles">
        <p><strong>Abhinav Datt</strong></p>
        <p>Visualization Expert</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="roles">
        <p><strong>Spandan Dahal</strong></p>
        <p>Model Developer</p>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown("""
    <div class="roles">
        <p><strong>Jatin Dadhyan</strong></p>
        <p>Project Coordinator</p>
    </div>
    """, unsafe_allow_html=True)
