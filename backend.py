import requests

key = "a5ac512a54654c8e7c9c1e1e6b57d781"

def get_data(place, forecast_days=None, data_type=None):
    # Zhukovskiy 462755
    url = "http://api.openweathermap.org/data/2.5/forecast?" \
          f"q={place}&" \
          f"appid={key}"
    response = requests.get(url)
    data = response.json()
    filtered_data = data['list'][:8*forecast_days] # filter data by number of obs.
    if data_type == "Temperature":
        filtered_data = [i["main"]["temp"] for i in filtered_data]
    if data_type == 'Sky':
        filtered_data = [i["weather"][0]["main"] for i in filtered_data]
    return filtered_data

if __name__ == "__main__":
    print(get_data(place="Zhukovskiy", forecast_days=3, data_type='Temperature'))
