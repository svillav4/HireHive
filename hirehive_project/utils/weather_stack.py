import requests
import dotenv
import os

# Cargar las variables de entorno desde el archivo .env
dotenv.load_dotenv()

# Obtener la clave de API de las variables de entorno
api_key = os.getenv("WEATHER_API_KEY")

def get_weather_data():
    url = "https://api.weatherstack.com/current?access_key=61b91c5214621236db78435efd2cb3d0"
    querystring = {"query":"Medellin"}
    response = requests.get(url, params=querystring)
    temp = response.json()["current"]["temperature"]

    return temp