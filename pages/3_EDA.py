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

# Section 1: Distribution of Cars by Fuel Type
st.image("images/Picture5.jpg", width=800)
st.markdown("""
    <div style="font-size: 24px; line-height: 1.8; color: #333;">
        <p>This bar chart shows the number of vehicles by fuel type in the dataset.</p>
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

# Section 2: Average Price vs. Make
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
        margin-top: 50px; 
        margin-bottom: 30px;">
        Average Price vs. Make
    </div>
""", unsafe_allow_html=True)

st.image("images/avg price vs make.jpg", width=800)
st.markdown("""
    <div style="font-size: 24px; line-height: 1.8; color: #333;">
        <p>The bar chart displays the average price of vehicles by car make, showing significant price variation between brands.</p>
        <ul>
            <li><b>Maserati and Rivian</b> stand out with the highest average prices, exceeding $120,000.</li>
            <li><b>Porsche, Mercedes-Benz, and Land Rover</b> also have relatively high average prices, positioning them among the luxury brands.</li>
            <li><b>More affordable brands</b> like Kia, Hyundai, and Ford are toward the lower end of the price range.</li>
        </ul>
        <h3 style="font-size: 24px; font-weight: bold; color: #5C4033;">Conclusion:</h3>
        <p>The data highlights the price disparities among car brands, emphasizing the market segmentation between luxury and economy vehicles.</p>
    </div>
""", unsafe_allow_html=True)

# Section 3: Average Days on Market by Make
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
        margin-top: 50px; 
        margin-bottom: 30px;">
        Average Days on Market by Car Make
    </div>
""", unsafe_allow_html=True)

st.image("images/avg days on market by make.jpg", width=800)
st.markdown("""
    <div style="font-size: 24px; line-height: 1.8; color: #333;">
        <p>The bar chart displays the average days on market for the top 10 car makes, highlighting how long, on average, vehicles from each make stay on the market before being sold.</p>
        <ul>
            <li><b>Ram vehicles</b> have the longest average days on market, exceeding 80 days.</li>
            <li><b>Toyota</b> has the shortest time on the market, with vehicles averaging less than 30 days.</li>
        </ul>
        <h3 style="font-size: 24px; font-weight: bold; color: #5C4033;">Conclusion:</h3>
        <p>This data underscores the varying levels of demand for different car makes, with Toyota having the quickest turnover and Ram taking significantly longer.</p>
    </div>
""", unsafe_allow_html=True)

# Section 4: Average Days on Market by Audi Model
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
        margin-top: 50px; 
        margin-bottom: 30px;">
        Average Days on Market by Audi Model
    </div>
""", unsafe_allow_html=True)

st.image("images/Picture6.jpg", width=800)
st.markdown("""
    <div style="font-size: 24px; line-height: 1.8; color: #333;">
        <p>The second chart breaks down the average days on market for different Audi models, showing significant variation in how long different models stay on the market.</p>
        <ul>
            <li><b>Audi SQ 8 e-tron</b> and <b>e-tron GT</b> have the longest average days on the market, indicating these models take the most time to sell.</li>
            <li>Models like the <b>Audi S8</b> and <b>TT RS</b> have much shorter average days on market, suggesting quicker sales.</li>
        </ul>
        <h3 style="font-size: 24px; font-weight: bold; color: #5C4033;">Conclusion:</h3>
        <p>The data highlights the differing demand levels for Audi models, with some high-performance or electric models taking longer to sell compared to others.</p>
    </div>
""", unsafe_allow_html=True)

# Section 5: Correlation Heatmap
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
        margin-top: 50px; 
        margin-bottom: 30px;">
        Correlation Heatmap
    </div>
""", unsafe_allow_html=True)

st.image("images/Heatmap.jpg", width=800)
st.markdown("""
    <div style="font-size: 24px; line-height: 1.8; color: #333;">
        <p>The heatmap illustrates the correlation between key numerical features in the dataset:</p>
        <ul>
            <li><b>Price and Mileage (-0.58):</b> Strong negative correlation indicates that vehicles with higher mileage tend to have lower prices.</li>
            <li><b>Price and Days on Market (+0.10):</b> Weak positive correlation suggests higher-priced vehicles may stay on the market slightly longer.</li>
            <li><b>Price and Model Year (+0.58):</b> Moderate positive correlation shows that newer vehicles (higher model year) tend to have higher prices.</li>
            <li><b>Mileage and Model Year (-0.84):</b> Strong negative correlation indicates older vehicles (lower model year) tend to have higher mileage.</li>
            <li><b>Days on Market and Mileage (-0.10):</b> Weak negative correlation suggests vehicles with higher mileage might sell slightly faster.</li>
            <li><b>Days on Market and Model Year (+0.09):</b> Very weak positive correlation suggests newer vehicles might stay on the market slightly longer.</li>
        </ul>
    </div>
""", unsafe_allow_html=True)
