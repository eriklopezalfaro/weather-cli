import datetime as dt
import requests

BASE_URL = 'http://api.openweathermap.org/data/2.5/weather?'
API_KEY = open('api_key.txt', 'r').read()
CITY = 'London'
COUNTRY = 'uk'

url = BASE_URL + 'q=' + CITY + '&APPID=dd3c88974a05a9da4c9a775c0049a127'
response = requests.get(url).json()

print(response)