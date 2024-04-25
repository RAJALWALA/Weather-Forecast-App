import streamlit as st

st.title("Weather forcast for the next few days")
place = st.text_input("place...")
days = st.slider("Forcast Days",min_value=1,max_value=5,
                 help="number of days to be forecasted")
options = st.selectbox("Select date to view",
                      ("temperature","sky"))
st.subheader(f"{options} for the next {days} days in {place}")