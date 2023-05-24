import streamlit as st
import plotly.express as px
from backend import get_data

# 288 Video
st.title('Weather Forecast for the Next Days')
place = st.text_input('Place: ') # capture value in a variable
days = st.slider('Forecast Days', min_value=1, max_value=5,
                 help='Select the number of forecasted days')
option = st.selectbox('Select data to view', ('Temperature', 'Sky'))


# 289 Video
# create a plotly figure to insert into streamlit plotly graph widget

# Get data from function
if place:
    try:
        filtered_data = get_data(place, days)
# 296 Video
# Create a temperature or sky plot
        if option == "Temperature":
            st.subheader(f'{option} for the next {days} days in {place}')
            temperatures = [(i["main"]["temp"]/10-32)*5/9 for i in filtered_data]
            dates = [i["dt_txt"] for i in filtered_data]
            figure = px.line(x=dates, y=temperatures,
                             labels={"x":"Date", "y":f"{option}"}) # x, y - array type objects
            st.plotly_chart(figure)
        if option == "Sky":
            st.subheader(f'{option} for the next {days} days in {place}')
            sky_conditions = [i["weather"][0]["main"] for i in filtered_data]
            sky_images = {'Rain':"images/rain.png",
                        'Clear':"images/clear.png",
                        "Snow":"images/snow.png",
                        "Clouds":"images/cloud.png"}
            image_paths = [sky_images[condition] for condition in sky_conditions]
            st.image(image_paths, width=150)
    except KeyError:
        st.subheader('No such city in the world, please retry your input')