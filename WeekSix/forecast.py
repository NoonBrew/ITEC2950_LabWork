import os
import requests
from datetime import datetime

key = os.environ.get('WEATHER_KEY')
query = {'q': 'minneapolis,us', 'units': 'imperial', 'appid': key}

url = 'https://api.openweathermap.org/data/2.5/forecast'

data = requests.get(url, params=query).json()

list_of_forecasts = data['list']

for forecast in list_of_forecasts:
    temp = forecast['main']['temp']
    time_stamp = forecast['dt']
    forecast_date = datetime.fromtimestamp(time_stamp)
    print(f'At {forecast_date} the temperature will be {temp}F')
