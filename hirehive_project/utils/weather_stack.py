import requests
import dotenv
import os
from ..interfaces import WeatherInterface

dotenv.load_dotenv()

class WeatherStackProvider(WeatherInterface):
    def __init__(self):
        self.api_key = os.getenv("WEATHER_API_KEY")

    def get_weather(self, city):
        url = f"http://api.weatherstack.com/current?access_key={self.api_key}&query={city}"
        querystring = {"query":"Medellin"}
        response = requests.get(url, params=querystring)
        data = response.json()
        if "current" in data:
            return data["current"]["temperature"]
        else:
            raise Exception("Error fetching weather data")