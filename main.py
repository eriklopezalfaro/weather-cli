import datetime as dt
import requests

BASE_URL = 'http://api.openweathermap.org/data/2.5/weather?'
API_KEY = open('api_key.txt', 'r').read()
CITY = 'London'
COUNTRY = 'uk'

def kelvin_to_celsius_fahrenheit(kelvin):
    celsius = kelvin - 273.15
    fahrenheit = celsius * (9/5) + 32
    return celsius, fahrenheit

url = BASE_URL + 'q=' + CITY + '&APPID=dd3c88974a05a9da4c9a775c0049a127'
response = requests.get(url).json()

# print(response)
temp_kelvin = response['main']['temp']
temp_celsius, temp_fahrenheit = kelvin_to_celsius_fahrenheit(temp_kelvin)
print(temp_celsius, temp_fahrenheit)

feels_like_kelvin = response['main']['feels_like']
feels_c, feels_f = kelvin_to_celsius_fahrenheit(feels_like_kelvin)

print(feels_c, feels_f)

