import os
import requests
import logging
from pprint import pprint

forecast_url = f'https://api.openweathermap.org/data/2.5/forecast'
weather_key = os.environ.get('WEATHER_KEY')
forecast_details_dict = {} # Holds Temp, Wind Speed and description with the Date Time as the key
forecast_dict_key_list = [] # Holds the datetime as the key to ensure, might not need.
logging.basicConfig(filename='forecast_debug.log', level=logging.DEBUG, format=f'%(asctime)s - %(name)s - %(levelname)s - %(message)s')

def main():

    location = get_location()
    scale, scale_choice = get_scale() # Return scale choice so we know how to format the output.
    forecast_list, error = get_forecast_data(location, scale)
    get_temp(forecast_list)
    get_weather_desc(forecast_list)
    get_wind_speed(forecast_list)
    display_forecast(forecast_details_dict, scale_choice) 
    

def get_location():
    city, country = '', ''
    while len(city) == 0:
        city = input('Enter the name of the city: ').strip()

    while len(country) != 2 or not country.isalpha():
        country = input('Enter the 2-letter country code: ').strip()

    location = f'{city},{country}'
    return location

def get_scale():
    scale_choice = ''
    scale = ''
    while scale_choice != 'f' and scale_choice != 'c': 
        scale_choice = input('For Celcius enter "C" or for Farhenheit enter "F": ').lower()
    if scale_choice == 'f':
        scale = 'imperial'
    elif scale_choice == 'c':
        scale = 'metric'
    return scale, scale_choice # Scale_choice 'F' = imperaial and 'C' = metric

def get_forecast_data(location, scale):
    try:
        query = {'q': location, 'units': scale, 'appid': weather_key }
        url_response = requests.get(forecast_url, params=query)
        url_response.raise_for_status() # raises HTTP error if one is occured.
        forecast_data = url_response.json()
        forecast_list = forecast_data['list']
        return forecast_list, None
    except Exception as ex:
        logging.exception(f'Error retriving weather data {ex}')
        logging.info(f'Url error response {url_response.text}')
        return None, ex

def get_temp(forecast_list):
    
    try:
        for forecast in forecast_list:
            forecast_details_dict[forecast['dt_txt']] = [forecast['main']['temp']]
    except KeyError:
        logging.error('get_temp did not recieved data in the expected format.')

def get_weather_desc(forecast_list):
    try:
        for forecast in forecast_list:
            weather_description = forecast['weather'][0]['description']
            forecast_details_dict[forecast['dt_txt']].append(weather_description) 
    except KeyError:
        logging.error('get_weather_desc did not recieved data in the expected format.')

def get_wind_speed(forecast_list):
    try:
        for forecast in forecast_list:
            wind_speed = forecast['wind']['speed']
            forecast_details_dict[forecast['dt_txt']].append(wind_speed)
    except KeyError:
        logging.error('get_wind_speed did not recieved data in the expected format.')

def display_forecast(forecast_details_dict, scale_choice):
    speed_units = ''
    temp_units = ''
    if scale_choice == 'f':
        speed_units = 'mph'
        temp_units = 'F'
    elif scale_choice == 'c':
        speed_units = 'm/s'
        temp_units = 'C'
    # details_list: index 0 - Temp, index 1 - Weather description, index 2 - Wind speeds. 
    for datetime, detail_list in forecast_details_dict.items():
        print('*'*20)
        # Using UTC for time. It is the default output from the JSON data. This allows the program to be more flexible when calling for different time zones
        # This also saves us from having to figure out the timezone of the location being called and formating the date to fit that time zone.
        print(f'Forecast for {datetime} UTC')
        print(f'Temperature: {detail_list[0]} {temp_units}.')
        print(f'Description: {detail_list[1]}.')
        print(f'Wind speed: {detail_list[2]} {speed_units}.')

if __name__ == '__main__':
    main()