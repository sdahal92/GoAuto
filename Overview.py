import streamlit as st

# Page Configuration
st.set_page_config(page_title="Go Norquest Overview", page_icon="🚗", layout="wide")

# Header Section with Images and Title
col1, col2, col3 = st.columns([1, 2, 1])  # Column layout for header

with col1:
    st.image("images/Go_Auto.jpg", width=130)  # Adjust width for smaller size

with col2:
    st.markdown(
        "<h1 style='text-align: center; color: #333;'>Overview Page</h1>", 
        unsafe_allow_html=True
    )  # Centered title with styling

with col3:
    st.image("images/Norquest Logo.jpeg", width=130)  # Adjust width for smaller size

# Welcome Message Section
st.write("")  # Spacer
st.markdown(
    """
    <div style="text-align: center; margin-top: 20px;">
        <h2 style="color: #4CAF50;">Welcome to Go Norquest!</h2>
        <p style="font-size: 18px; color: #555;">
        This project leverages cutting-edge data science and machine learning to provide actionable insights into vehicle sales trends. 
        Explore our data-driven strategies and AI-powered tools to optimize dealership performance.
        </p>
    </div>
    """,
    unsafe_allow_html=True,
)

# Highlights Section
st.markdown("### Project Highlights")  # Section Title

# Columns for Highlights
highlight_col1, highlight_col2, highlight_col3 = st.columns(3)

with highlight_col1:
    st.image("images/highlight1.jpg", caption="Data Insights", use_column_width=True)
    st.markdown("<p style='text-align: center;'>Deep insights into sales trends.</p>", unsafe_allow_html=True)

with highlight_col2:
    st.image("images/highlight2.jpg", caption="AI Models", use_column_width=True)
    st.markdown("<p style='text-align: center;'>AI-powered predictions.</p>", unsafe_allow_html=True)

with highlight_col3:
    st.image("images/highlight3.jpg", caption="Customer Analysis", use_column_width=True)
    st.markdown("<p style='text-align: center;'>Customer preference analysis.</p>", unsafe_allow_html=True)

# Footer Section
st.markdown(
    """
    <hr style="margin-top: 50px;">
    <footer style="text-align: center; font-size: 14px; color: #777;">
        <p>© 2024 Go Norquest. Empowering Dealerships with AI and Data Insights.</p>
    </footer>
    """,
    unsafe_allow_html=True,
)
