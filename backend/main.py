import json
import jsonpickle
import requests
from flask_cors import CORS, cross_origin
from flask import Flask, jsonify, request

from SECRET import keys 
from weather import Weather, calculate_weather
import temperature
from openweather import get_current_openweather
from darksky import get_current_darksky, get_future_weather_darksky
from constants import LATITUDE, LONGITUDE



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