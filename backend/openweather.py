import json
import jsonpickle
import requests
from SECRET import keys 
from weather import Weather, calculate_weather
import temperature
from constants import LATITUDE, LONGITUDE

def get_current_openweather(lat, lon):
    """
    get current weather details from openweathermap API
    """
    api_key = keys['openweather']
    ENDPOINT = 'http://api.openweathermap.org/data/2.5/weather?'
    url = ENDPOINT + 'appid=' + api_key
    url += '&lat=' + lat
    url += '&lon=' + lon
    print(url)
    response = requests.get(url)    
    if response.status_code == 200:
        data = json.loads(response.text)
        current_weather = data.get("main")
        temp = current_weather["temp"]
        hum = current_weather["humidity"]
        pre = current_weather["pressure"]
        con = data.get("weather")[0].get("description")
        icon = data.get("weather")[0].get("icon")
        w_obj = Weather(lat, lon, temp, hum, pre, con, icon)
        return w_obj
    else:
        print(response.text)
        print("FAILED")