# Methods to fetch data from darksky API
import json
import jsonpickle
import requests
from SECRET import keys 
from weather import Weather, calculate_weather
import temperature
from constants import LATITUDE, LONGITUDE

def get_current_darksky(lat, lon):
    """
    Get current wether details from darksky APIs
    """
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


def get_future_weather_darksky(lst):
    """
    Get future weather data from darksky
    """
    if lst is None:
        return []
    ans = []
    for data in lst[1:]:
        time = data["time"]
        temp = round((data["temperatureHigh"] + data["temperatureLow"]) / 2, 1)
        dic = {"time": time, "temp": temp}
        ans.append(dic)
    return ans