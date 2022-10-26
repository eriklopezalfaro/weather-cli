import datetime as dt
import os

import requests
from dotenv import load_dotenv


# API_KEY = open('api_key.txt', 'r').read()
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather?'
CITY = 'London'
# API_KEY = os.getenv('api_key')
# print(API_KEY)

def configure():
    load_dotenv()

def kelvin_to_celsius_fahrenheit(kelvin):
    celsius = kelvin - 273.15
    fahrenheit = celsius * (9/5) + 32
    return celsius, fahrenheit

def main():
    configure()
    # url = BASE_URL + 'q=' + CITY + '&APPID=dd3c88974a05a9da4c9a775c0049a127'
    url = f'{BASE_URL}q={CITY}&APPID={os.getenv("api_key")}'
    response = requests.get(url).json()

    print(response)

    # temp_kelvin = response['main']['temp']
    # temp_celsius, temp_fahrenheit = kelvin_to_celsius_fahrenheit(temp_kelvin)
    # print(temp_celsius, temp_fahrenheit)

    # feels_like_kelvin = response['main']['feels_like']
    # feels_c, feels_f = kelvin_to_celsius_fahrenheit(feels_like_kelvin)
    # print(feels_c, feels_f)

    # humidity, description, sunrise

    # todo
    # make into functions, config, dotenv, init, comment code, requests



if __name__ == '__main__':
    main()

