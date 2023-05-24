import streamlit as st
import plotly.express as px
from backend import get_data

# 288 Video
st.title('Wheather Forecast for the Next Days')
place = st.text_input('Place: ') # capture value in a variable
days = st.slider('Forecast Days', min_value=1, max_value=5,
                 help='Select the number of forecasted days')
option = st.selectbox('Select data to view', ('Temperature', 'Sky'))
st.subheader(f'{option} for the next {days} days in {place}')

# 289 Video
# create a plotly figure to insert into streamlit plotly graph widget

#293
data = get_data(place, days, option)

figure = px.line(x=days, y=option,
                 labels={"x":"Date", "y":f"{option}"}) # x, y - array type objects
st.plotly_chart(figure)