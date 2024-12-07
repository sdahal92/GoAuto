import streamlit as st

# Header with Images in Top-Left and Top-Right Corners
col1, col2, col3 = st.columns([1, 2, 1])  # Adjust column widths as needed

with col1:
    st.image("images/Go_Auto.jpg", width=130)  # Adjust width for smaller size

with col2:
    st.markdown("<h1 style='text-align: center;'>Overview Page</h1>", unsafe_allow_html=True)  # Centered title

with col3:
    st.image("images/Norquest Logo.jpeg", width=130, )  # Adjust width for smaller size

# Additional Content Below the Header
st.write("Welcome to the Overview page of Go Norquest!")
