import streamlit as st

# Set page configuration
st.set_page_config(page_title="Power BI Dashboard", layout="wide")

# Title with clickable link
st.markdown("""
    <div style="
        text-align: center; 
        background-color: #FFDAB9; 
        color: #5C4033; 
        padding: 20px; 
        border-radius: 15px; 
        box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.1);
        font-size: 2rem;
        font-weight: bold;
        margin-bottom: 30px;">
        <a href="https://norquest-my.sharepoint.com/:u:/g/personal/sdahal92_norquest_ca/EWZX0HGfzTpNukdqaNQ8Bg8BoJXSAaj054f0qkfEm86s9w?e=0M8zgC" 
           style="text-decoration: none; color: #5C4033;">
           Power BI Dashboard
        </a>
    </div>
""", unsafe_allow_html=True)

# Embed the Power BI dashboard
st.markdown("""
    <iframe 
        src="https://app.powerbi.com/reportEmbed?reportId=33e3725d-78e3-40d8-8c93-f414f39a832c&autoAuth=true&ctid=2ba011f1-f50a-44f3-a200-db3ea74e29b7" 
        width="100%" 
        height="800px" 
        frameborder="0" 
        allowFullScreen="true">
    </iframe>
""", unsafe_allow_html=True)

# Description of the dashboard
st.markdown("""
    <div style="font-size: 18px; color: #555; margin-top: 20px;">
        This interactive dashboard, developed using Power BI, provides a comprehensive overview of the vehicle dataset. 
        Users can explore trends, identify patterns, and analyze key metrics through dynamic visualizations.
    </div>
""", unsafe_allow_html=True)
