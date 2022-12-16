import requests


def get_weather():
    return requests.get("https://api.open-meteo.com/v1/forecast?latitude=44.4268&longitude=26.1025&current_weather=true&hourly=temperature_2m,relativehumidity_2m,windspeed_10m")
