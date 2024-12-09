import streamlit as st

# Title inside a styled box with gap
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
        Exploratory Data Analysis (EDA)
    </div>
    <br><br>
""", unsafe_allow_html=True)

# Display the image with adjusted width
st.image("images/Picture5.jpg", width=800)

# Description for the chart with font size set to 24px
st.markdown("""
    <div style="font-size: 24px; line-height: 1.8; color: #333;">
        <p style="font-size: 20px;>This bar chart shows the number of vehicles by fuel type in the dataset.</p>
        <ul>
            <li><b>Gasoline Vehicles</b>: The majority, with 124,029 cars, dominate the dataset.</li>
            <li><b>Diesel</b>: There are 8,632 diesel cars, the second-largest category.</li>
            <li><b>Electric</b>: 5,023 electric vehicles reflect growing interest, though still smaller than gas and diesel.</li>
            <li><b>Hybrid and PHEV</b>: 4,442 hybrid and 2,979 plug-in hybrids indicate some demand for fuel-efficient options.</li>
            <li><b>CNG and Hydrogen</b>: These fuel types are rare, with only 6 CNG and 3 hydrogen vehicles.</li>
        </ul>
        <h3 style="font-size: 24px; font-weight: bold; color: #5C4033;">Conclusion:</h3>
        <p>Gasoline vehicles are the largest group, with other fuel types present in much smaller numbers, highlighting the continued dominance of traditional fuel in the market.</p>
    </div>
""", unsafe_allow_html=True)
