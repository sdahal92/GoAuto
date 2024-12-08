import streamlit as st

# Header with Images in Top-Left and Top-Right Corners
col1, col2, col3 = st.columns([1, 2, 1])  # Adjust column widths as needed

with col1:
    st.image("images/Go_Auto.jpg", width=130)  # Adjust width for smaller size

with col2:
    st.markdown("<h1 style='text-align: center;'>Overview Page</h1>", unsafe_allow_html=True)  # Centered title

with col3:
    st.image("images/Norquest Logo.jpeg", width=130)  # Adjust width for smaller size

# Welcome Section
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

# Project Highlights Section Without Images
st.markdown("### Project Highlights")  # Section Title

# Highlight Text in Columns (No Images)
highlight_col1, highlight_col2, highlight_col3 = st.columns(3)

with highlight_col1:
    st.markdown(
        "<p style='text-align: center; font-size: 18px;'>Deep insights into sales trends.</p>", 
        unsafe_allow_html=True
    )

with highlight_col2:
    st.markdown(
        "<p style='text-align: center; font-size: 18px;'>AI-powered predictions.</p>", 
        unsafe_allow_html=True
    )

with highlight_col3:
    st.markdown(
        "<p style='text-align: center; font-size: 18px;'>Customer preference analysis.</p>", 
        unsafe_allow_html=True
    )
