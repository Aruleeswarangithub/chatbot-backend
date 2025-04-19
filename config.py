import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Fetch your API key from the environment
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY", "YOUR_FALLBACK_API_KEY")
WEATHER_API_KEY = os.getenv("WEATHER_API_KEY", "YOUR_FALLBACK_WEATHER_API_KEY")

# Now you can use WEATHER_API_KEY and GOOGLE_API_KEY as needed
print("Google API Key:", GOOGLE_API_KEY)
print("Weather API Key:", WEATHER_API_KEY)
