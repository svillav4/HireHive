from ..interfaces import WeatherInterface

class StaticWeatherProvider(WeatherInterface):
    def get_weather(self):
        # Static data for testing dependency injection
        medellin_temperature = 23
        return medellin_temperature