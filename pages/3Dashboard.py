import streamlit as st

# Set page configuration
st.set_page_config(page_title="EDA - Power BI Dashboard", layout="wide")

# Title for the EDA page, centered
st.markdown("""
    <h1 style="text-align: center; color: black;">Power BI Dashboard</h1>
""", unsafe_allow_html=True)

# Embed the Power BI dashboard
st.markdown("""
    <div style="display: flex; justify-content: center; align-items: center; margin-top: 20px;">
        <iframe 
            src="https://app.powerbi.com/reportEmbed?reportId=33e3725d-78e3-40d8-8c93-f414f39a832c&autoAuth=true&ctid=2ba011f1-f50a-44f3-a200-db3ea74e29b7" 
            width="100%" 
            height="800px" 
            frameborder="0" 
            allowFullScreen="true">
        </iframe>
    </div>
""", unsafe_allow_html=True)
