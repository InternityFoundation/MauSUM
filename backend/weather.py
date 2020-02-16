import hashlib
import json
import jsonpickle
import sys
import requests
import time
from flask_cors import CORS, cross_origin
from uuid import uuid4
from urllib.parse import urlparse
from flask import Flask, jsonify, request, render_template

from SECRET import keys 
import temperature

#CONSTANTS
LATITUDE = 'latitude'
LONGITUDE = 'longitude'

class Weather:
    def __init__(self, lat, lon, temp, hum, pre, con="", icon=""):
        self.latitude = lat
        self.longitude = lon
        self.temperature = round(temp, 1)
        self.humidity = round(hum, 1)
        self.pressure = round(pre, 1)
        self.condition = con
        self.icon = icon
        self.future = []
        self.time = time.time()

    def set_future_data(self, data):
        if data is not None:
            self.future = data

    def __str__(self):
        return str("Lat: %s Long: %s Temp: %s icon: %s" %(self.latitude, self.longitude, self.temperature, self.icon))

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True, indent=4)


def calculate_weather(weather_obj_list):
    """
    It Averages weather received from various data source and generate final weather output
    """
    temp = 0
    hum = 0
    count = 0
    pre = 0
    icon = ""
    con = ""
    future = []
    for weather in weather_obj_list:
        print(weather)
        if weather is None:
            continue
        lat = weather.latitude
        lon = weather.longitude
        if weather.icon != "":
            icon = weather.icon
        if weather.condition != "":
            con = weather.condition
        if len(weather.future) > 0:
            future = weather.future
        temp += weather.temperature
        hum += weather.humidity
        pre += weather.pressure
        count += 1
    temp /= count
    hum /= count
    pre /= count

    cal_weather_obj = Weather(lat, lon, temp, hum, pre, con, icon)
    cal_weather_obj.set_future_data(future)
    return cal_weather_obj

def get_future_weather_darksky(lst):
    if lst is None:
        return []
    ans = []
    for data in lst:
        time = data["time"]
        temp = round((data["temperatureHigh"] + data["temperatureLow"]) / 2, 1)
        dic = {"time": time, "temp": temp}
        ans.append(dic)
    return ans

def get_current_darksky(lat, lon):
    api_key = keys['darksky']
    ENDPOINT = 'https://api.darksky.net/forecast/' + api_key + '/'

    url = ENDPOINT + lat + ',' + lon +'?units=si'
    response = requests.get(url)
    if response.status_code == 200:
        data = json.loads(response.text)
        current_weather = data["currently"]
        temp = current_weather["temperature"]
        temp = temperature.celsius_to_kelvin(temp)
        hum = current_weather["humidity"]
        pre = current_weather["pressure"]
        w_obj = Weather(lat, lon, temp, hum, pre)
        future_data = get_future_weather_darksky(data["daily"]["data"]);
        w_obj.set_future_data(future_data)
        return w_obj
    else:
        print("FAILED")


def get_current_openweather(lat, lon):
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

app = Flask(__name__, static_url_path='')
cors = CORS(app)

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
    weather_obj_list.append(get_current_darksky(lat, lon))
    weather_obj_list.append(get_current_openweather(lat, lon))
    weather = calculate_weather(weather_obj_list)
    response = jsonpickle.encode(weather, unpicklable=False)

    return response, 200


if __name__ == '__main__':
    try:
        port_no = sys.argv[1]
    except:
        port_no = 8000
    app.run(debug=True, port=port_no)
