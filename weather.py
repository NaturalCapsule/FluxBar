import requests
from configparser import ConfigParser

class Weather:
    def __init__(self):
        self.config = ConfigParser()
        self.config.read("config/config.ini")
        api_key = self.config.get("Panel", "weather_api_key")
        city = self.config.get("Panel", "city")
        
        url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'
        self.response = requests.get(url)
        # if self.response.status_code == 200:
        self.data = self.response.json()
        # else:
        #     return "Error fetching weather data"
        
    def get_city(self):
        self.city = self.config.get("Panel", "city")
        return self.city

    def get_temp(self):
        if 'main' in self.data:
            temp = self.data['main']['temp']
            temp -= 273  # Convert from Kelvin to Celsius
            return f"Temperature: {temp:.2f} °C"
        else:
            return "Temperature data not available (you got to wait a few minutes/hours for the api to active)"

    
    def get_sky(self):
        description = self.data['weather'][0]['description']
        
        return f"Sky: {description}"
