import requests
import pandas as pd

API_KEY = "your_api_key_here"
CITY = "Mumbai"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

params = {
    'q': CITY,
    'appid': API_KEY,
    'units': 'metric'
}

response = requests.get(BASE_URL, params=params)

if response.status_code == 200:
    data = response.json()
    weather_info = {
        "City": data["name"],
        "Temperature (C)": data["main"]["temp"],
        "Humidity (%)": data["main"]["humidity"],
        "Weather": data["weather"][0]["description"],
        "Wind Speed (m/s)": data["wind"]["speed"]
    }
    df = pd.DataFrame([weather_info])
    df.to_csv("weather_data.csv", index=False)
    print("Data saved successfully to weather_data.csv")
else:
    print("Error:", response.status_code)
