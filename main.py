import streamlit as st
import plotly.express as px
from functions import get_data

st.title("Weather forcast for the next few days")
place = st.text_input("place...")
days = st.slider("Forcast Days",min_value=1,max_value=5,
                 help="number of days to be forecasted")
options = st.selectbox("Select date to view",
                      ("Temperature","Sky"))
st.subheader(f"{options} for the next {days} days in {place}")

if place:
    try:
        filtered_content = get_data(place, days)

        if options == "Temperature":
            temperatures = [dict["main"]["temp"]/ 10 for dict in filtered_content]
            dates = [dict["dt_txt"]for dict in filtered_content]
            figure = px.line(x=dates,y=temperatures,labels={"x":"dates","y":"temperatures (c)"})
            st.plotly_chart(figure)

        if options == "Sky":
            images = {"Clear": "images (2)/clear.png","Clouds":"images (2)/cloud.png",
                      "Rain":"images (2)/rain.png","Snow":""}
            sky_conditions = [dict["weather"][0]["main"] for dict in filtered_content]
            image_paths = [images[condition] for condition in sky_conditions]
            print(sky_conditions)
            st.image(image_paths,width=115)

    except KeyError:
        st.write("Wrong input")
