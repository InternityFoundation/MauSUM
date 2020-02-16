import time
from SECRET import keys 
import temperature
from constants import LATITUDE, LONGITUDE


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







