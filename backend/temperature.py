# Stores function related to temperature conversion
ROUND_TO = 2

def fahrenheit_to_kelvin(temp_f):
    return round((temp_f - 32) * (5 / 9) + 273.15, ROUND_TO)

def celsius_to_kelvin(temp_c):
    return round(temp_c + 273.15, ROUND_TO)

def kelvin_to_fahrenheit(temp_k):
    return round((temp_k - 273.15) * (9 / 5) + 32, ROUND_TO)

def kelvin_to_celsius(temp_k):
    return round(temp_k - 273.15, ROUND_TO)