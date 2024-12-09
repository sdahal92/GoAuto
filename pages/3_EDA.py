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
st.image("images/Picture5.jpg",  width=800)

# Description for the chart
st.write("""
This bar chart shows the number of vehicles by fuel type in the dataset.

- **Gasoline Vehicles**: The majority, with 124,029 cars, dominate the dataset.
- **Diesel**: There are 8,632 diesel cars, the second-largest category.
- **Electric**: 5,023 electric vehicles reflect growing interest, though still smaller than gas and diesel.
- **Hybrid and PHEV**: 4,442 hybrid and 2,979 plug-in hybrids indicate some demand for fuel-efficient options.
- **CNG and Hydrogen**: These fuel types are rare, with only 6 CNG and 3 hydrogen vehicles.

### Conclusion:
Gasoline vehicles are the largest group, with other fuel types present in much smaller numbers, highlighting the continued dominance of traditional fuel in the market.
""")
