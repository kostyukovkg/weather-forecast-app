import requests
import streamlit as st

# Everything is accessible via the st.secrets dict:
a = st.write("API key:", st.secrets["api_key"])

def get_data(place, forecast_days=None):
    # Zhukovskiy 462755
    url = "http://api.openweathermap.org/data/2.5/forecast?" \
          f"q={place}&" \
          f"appid={st.secrets['API key']}"
    response = requests.get(url)
    data = response.json()
    filtered_data = data['list'][:8*forecast_days] # filter data by number of obs.
    return filtered_data

if __name__ == "__main__":
    print(get_data(place="Zhukovskiy", forecast_days=3))
