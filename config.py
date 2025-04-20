# config.py
import os
from dotenv import load_dotenv

load_dotenv()

MAPBOX_API_KEY = os.getenv("MAPBOX_API_KEY", "YOUR_FALLBACK_MAPBOX_KEY")
WEATHER_API_KEY = os.getenv("WEATHER_API_KEY", "YOUR_FALLBACK_WEATHER_KEY")

print("Mapbox API Key:", MAPBOX_API_KEY)
print("Weather API Key:", WEATHER_API_KEY)
