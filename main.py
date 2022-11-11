import datetime as dt
import os
import sys
from pprint import pp


import requests
from dotenv import load_dotenv


BASE_URL = 'http://api.openweathermap.org/data/2.5/weather?'
CITY = sys.argv[1] #validate and could be more arguments

print(f'\n1:{CITY}, 2:{sys.argv[0]}\n')

def configure():
    load_dotenv()  

def kelvin_to_celsius_fahrenheit(kelvin):
    celsius = kelvin - 273.15
    fahrenheit = celsius * (9/5) + 32
    return celsius, fahrenheit

def main():
    configure()
    
    url = f'{BASE_URL}q={CITY}&APPID={os.getenv("api_key")}'

    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.exceptions.HTTPError as err:
        print("Http Error:", err)
        sys.exit('Try agin with Valid city.')

    response = response.json()
    pp(response, indent=4)
    description = response['weather'][0]['description']
    temp_kelvin = response['main']['temp']
    temp_celsius, temp_fahrenheit = kelvin_to_celsius_fahrenheit(temp_kelvin)
    print(f'\n{CITY}: {temp_celsius}°C / {temp_fahrenheit}°F {description}\n')


    # humidity, description, sunrise, datetune will be added to full end

    # todo
    # comment code



if __name__ == '__main__':
    main()

