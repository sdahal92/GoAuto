import streamlit as st

# --- Custom Page Config ---
st.set_page_config(
    page_title="Go Norquest Overview",  # Browser tab title
    page_icon="🚗",  # Icon for the app
    layout="wide",  # Use the entire width of the page
)

# --- Header Section with Logos and Title ---
st.markdown(
    """
    <style>
    .header {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 10px 20px;
        background-color: #f1f1f1; /* Light gray background */
        border-bottom: 2px solid #ddd; /* Bottom border */
    }
    .header img {
        max-width: 120px; /* Resize images */
        height: auto;
    }
    .header h1 {
        flex-grow: 1;
        text-align: center;
        font-size: 32px;
        color: #333; /* Dark gray */
        margin: 0;
    }
    </style>
    <div class="header">
        <img src="images/Go_Auto.jpg" alt="Go Auto Logo">
        <h1>Overview Page</h1>
        <img src="images/Norquest Logo.jpeg" alt="Norquest Logo">
    </div>
    """,
    unsafe_allow_html=True
)

# --- Main Section ---
st.write("")  # Spacer
st.markdown("<h2 style='text-align: center;'>Welcome to Go Norquest!</h2>", unsafe_allow_html=True)

# Section with description
st.markdown(
    """
    <p style="text-align: center; font-size: 18px; color: #555;">
    This project leverages data science and machine learning techniques to analyze Go Auto vehicle sales. 
    Dive into the data, explore trends, and learn how we optimize dealership performance with AI-powered solutions.
    </p>
    """,
    unsafe_allow_html=True,
)

# --- Featured Highlights Section ---
st.markdown("### Project Highlights")
col1, col2, col3 = st.columns(3)

with col1:
    st.image("images/highlight1.jpg", caption="Data Insights", width=250)
    st.markdown("<p style='text-align: center;'>Deep insights into sales trends.</p>", unsafe_allow_html=True)

with col2:
    st.image("images/highlight2.jpg", caption="AI Models", width=250)
    st.markdown("<p style='text-align: center;'>AI-powered predictions.</p>", unsafe_allow_html=True)

with col3:
    st.image("images/highlight3.jpg", caption="Customer Analysis", width=250)
    st.markdown("<p style='text-align: center;'>Customer preference analysis.</p>", unsafe_allow_html=True)

# --- Background Color and Footer ---
st.markdown(
    """
    <style>
    body {
        background-color: #f9f9f9; /* Light gray for a modern look */
    }
    footer {
        font-size: 14px;
        text-align: center;
        padding: 10px;
        color: #777;
        border-top: 1px solid #ddd;
    }
    </style>
    <footer>
    © 2024 Go Norquest. Empowering Dealerships with AI and Data Insights.
    </footer>
    """,
    unsafe_allow_html=True,
)
