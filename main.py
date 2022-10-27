import datetime as dt
import os
import sys

import requests
from dotenv import load_dotenv


# API_KEY = open('api_key.txt', 'r').read()
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather?'
CITY = sys.argv[1] #validate
# CITY = 'London'
print(f'1:{CITY}, 2:{sys.argv[0]}')

def configure():
    load_dotenv()
    # API_KEY = os.getenv('api_key')
    # print(API_KEY)

def kelvin_to_celsius_fahrenheit(kelvin):
    celsius = kelvin - 273.15
    fahrenheit = celsius * (9/5) + 32
    return celsius, fahrenheit

def main():
    configure()
    # url = BASE_URL + 'q=' + CITY + '&APPID=dd3c88974a05a9da4c9a775c0049a127'
    url = f'{BASE_URL}q={CITY}&APPID={os.getenv("api_key")}'
    response = requests.get(url).json() #make a try exept block

    print(f'\n{response}')

    description = response['weather'][0]['description']
    temp_kelvin = response['main']['temp']
    temp_celsius, temp_fahrenheit = kelvin_to_celsius_fahrenheit(temp_kelvin)
    
    print(f'\n{CITY}: {temp_celsius}°C / {temp_fahrenheit}°F \n{description}\n')

    # humidity, description, sunrise

    # todo
    # make into functions, config, dotenv, init, comment code, requests



if __name__ == '__main__':
    main()

