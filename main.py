import streamlit as st
import plotly.express as px

# 288 Video
st.title('Wheather Forecast for the Next Days')
place = st.text_input('Place: ') # capture value in a variable
days = st.slider('Forecast Days', min_value=1, max_value=5,
                 help='Select the number of forecasted days')
option = st.selectbox('Select data to view', ('Temperature', 'Sky'))
st.subheader(f'{option} for the next {days} days in {place}')

# 289 Video
# create a plotly figure to insert into streamlit plotly graph widget
dates = ["2022-25-10", "2022-25-11", "2022-25-12"]
temperatures = [20, 21, 22]

figure = px.line(x=dates, y=temperatures,
                 labels={"x":"Date", "y":"Temperature"}) # x, y - array type objects
st.plotly_chart(figure)