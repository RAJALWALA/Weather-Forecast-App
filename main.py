import streamlit as st
import plotly.express as px

st.title("Weather forcast for the next few days")
place = st.text_input("place...")
days = st.slider("Forcast Days",min_value=1,max_value=5,
                 help="number of days to be forecasted")
options = st.selectbox("Select date to view",
                      ("temperature","sky"))
st.subheader(f"{options} for the next {days} days in {place}")

def get_data(days):
    dates = ["2024-23-01","2024-13-01","2024-17-01"]
    temperatures = [10,11,18]
    temperatures = [days * i for i in temperatures]
    return dates,temperatures

d,t =get_data(days)

figure = px.line(x=d,y=t,labels={"x":"dates","y":"temperatures (c)"})
st.plotly_chart(figure)