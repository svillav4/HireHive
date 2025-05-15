from abc import ABC, abstractmethod

class WeatherInterface(ABC):
    @abstractmethod
    def get_weather(self) -> int:
        pass