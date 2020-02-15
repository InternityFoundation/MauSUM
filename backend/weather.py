import hashlib
import json
import jsonpickle
import sys
import requests
from time import time
from uuid import uuid4
from urllib.parse import urlparse
from flask import Flask, jsonify, request, render_template

from SECRET import keys 

#CONSTANTS
LATITUDE = 'latitude'
LONGITUDE = 'longitude'

class Weather:
    def __init__(self, lat, lon, temp, hum):
        self.latitude = lat
        self.longitude = lon
        self.temperature = temp
        self.humidity = hum
        self.time = "00"

    def __str__(self):
        return str("Lat: %s Long: %s Temp: %s" %(self.latitude, self.longitude, self.temperature))

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True, indent=4)


def calculate_weather(weather_obj_list):
    """
    It Averages weather received from various data source and generate final weather output
    """
    temp = 0
    hum = 0
    for weather in weather_obj_list:
        lat = weather.latitude
        lon = weather.longitude
        temp += weather.temperature
        hum += weather.humidity

    temp /= len(weather_obj_list)
    hum /= len(weather_obj_list)

    cal_weather_obj = Weather(lat, lon, temp, hum)
    return cal_weather_obj

def get_current_darksky(lat, lon):
    """
    api_key = keys['darksky']
    ENDPOINT = 'https://api.darksky.net/forecast/' + api_key + '/'

    url = ENDPOINT + lat + ',' + lon
    response = requests.get(url)
    if response.status_code == 200:
        data = json.loads(response.text)
        current_weather = data["currently"]
        temp = current_weather["temperature"]
        hum = current_weather["humidity"]
        w_obj = Weather(lat, lon, temp, hum)
        return w_obj
    else:
        print("FAILED")
    """
    with open('../data/darksky.json') as f:
        data = json.load(f)
        current_weather = data["currently"]
        temp = current_weather["temperature"]
        hum = current_weather["humidity"]
        w_obj = Weather(lat, lon, temp, hum)
        return w_obj

def get_current_openweather(lat, lon):
    api_key = keys['openweather']
    ENDPOINT = 'http://api.openweathermap.org/data/2.5/weather?q=Pune&'
    url = ENDPOINT + 'appid=' + api_key
    response = requests.get(url)    
    if response.status_code == 200:
        data = json.loads(response.text)
        current_weather = data.get("main")
        temp = current_weather["temp"]
        hum = current_weather["humidity"]
        w_obj = Weather(lat, lon, temp, hum)
        return w_obj
    else:
        print(response.text)
        print("FAILED")

app = Flask(__name__, static_url_path='')

@app.route('/weather', methods=['GET'])
def get_current_weather():
    """
    Based on lat & lon passed scrap data from various source and generate current weather
    """
    lat = request.args.get(LATITUDE)
    lon = request.args.get(LONGITUDE)
    if not lat or not lon:
        return 'Missing Values', 400
    weather_obj_list = list()
    darksky_obj = get_current_darksky(lat, lon)
    if darksky_obj is not None:
        weather_obj_list.append(darksky_obj)
    openweather_obj = get_current_openweather(lat, lon)
    if openweather_obj is not None:
        weather_obj_list.append(openweather_obj)
    weather = calculate_weather(weather_obj_list)
    print(weather)
    response = {
        'weather': jsonpickle.encode(weather, unpicklable=False)
    }

    return jsonify(response), 200


if __name__ == '__main__':
    try:
        port_no = sys.argv[1]
    except:
        port_no = 8000
    app.run(debug=True, port=port_no)
