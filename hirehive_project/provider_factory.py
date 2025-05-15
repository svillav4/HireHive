from .utils.weather_stack import WeatherStackProvider
from .utils.static_weather import StaticWeatherProvider

def get_weather_provider(provider_name: str):
    if provider_name == "weather_stack":
        return WeatherStackProvider()
    elif provider_name == "static":
        return StaticWeatherProvider()
    else:
        raise ValueError(f"Unknown provider: {provider_name}")