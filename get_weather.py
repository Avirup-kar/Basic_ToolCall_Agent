import requests
from dotenv import load_dotenv
import httpx
import os

load_dotenv()


WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")

async def call_weather(city: str):
    url = "https://api.weatherapi.com/v1/current.json"

    params = {
        "key": WEATHER_API_KEY,
        "q": city
    }

    async with httpx.AsyncClient() as client:
          response = await client.get(url, params=params)
          
    data = response.json()
    

    return {
        "city": data["location"]["name"],
        "temperature": data["current"]["temp_c"],
        "feels_like": data["current"]["feelslike_c"],
        "condition": data["current"]["condition"]["text"],
        "humidity": data["current"]["humidity"],
        "wind_kph": data["current"]["wind_kph"]
    }
