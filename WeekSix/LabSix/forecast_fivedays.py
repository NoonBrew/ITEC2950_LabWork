import os
import requests
from pprint import pprint

forecast_url = f'https://api.openweathermap.org/data/2.5/forecast'
weather_key = os.environ.get('WEATHER_KEY')

def main():

    location = get_location()
    scale = get_scale()
    forecast_list, error = get_forecast_data(location, scale)
    time_temp_dict = get_temp(forecast_list)
    print(time_temp_dict)
    ######
    ## TODO Make a get weather description function that creates a dictionary with key: Date time and value: description
    ## Also need to make a get a wind speed dictionary using the date time text as a key. Then create a function or use main to display the information from
    ## the dictionary. Then we can use an if else statement to verify each list is the same length and then grab the key from one dictionary and use it to access the other three
    ## Alternativly look at making a global dictionary that will have all threee values under the date key. This is probably better. 
    ## then address the time_choice. Look at the documentation for the API might be able to make the call with a param to get the time we want. 
    ##
    ## finally change errors to logging statements. Need to watch video on how to do that, save for saturday? 

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
    return scale

def get_forecast_data(location, scale):
    try:
        query = {'q': location, 'units': scale, 'appid': weather_key }
        url_response = requests.get(forecast_url, params=query)
        url_response.raise_for_status() # raises HTTP error if one is occured.
        forecast_data = url_response.json()
        forecast_list = forecast_data['list']
        return forecast_list, None
    except Exception as ex:
        print(ex)
        print(url_response.text)
        return None, ex

def get_temp(forecast_list):
    time_temp_dict = {}
    try:
        for forecast in forecast_list:
            time_temp_dict[forecast['dt_txt']] = forecast['main']['temp']
        return time_temp_dict
    except KeyError:
        print('Date is not in the expected format')
        return 'Unkown'

if __name__ == '__main__':
    main()