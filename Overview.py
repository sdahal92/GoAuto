import streamlit as st
import streamlit as st

# Custom HTML for the header
st.markdown(
    """
    <style>
    .header {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 10px 20px;
        background-color: #f8f9fa; /* Light background color for the header */
        border-bottom: 2px solid #ddd; /* Optional bottom border */
    }
    .header img {
        max-width: 120px; /* Set the maximum width for the images */
        height: auto; /* Maintain aspect ratio */
    }
    .header h1 {
        flex-grow: 1;
        text-align: center;
        font-size: 24px;
        color: #333; /* Text color */
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

# Add additional content below the header
st.write("Welcome to the Overview page of Go Norquest!")



