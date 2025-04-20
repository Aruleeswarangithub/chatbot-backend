# places_service.py
import requests
from config import MAPBOX_API_KEY

MAPBOX_GEOCODING_URL = "https://api.mapbox.com/geocoding/v5/mapbox.places"

def get_places_nearby(location, query, limit=10):
    """
    Query Mapbox Geocoding API for nearby places.
    Args:
        location (str): "lat,lng"
        query (str): search query like 'hospital', 'restaurant'
        limit (int): number of results
    Returns:
        List of dicts with keys: name, address, rating (None), location
    """
    lat, lng = location.split(',')

    url = f"{MAPBOX_GEOCODING_URL}/{query}.json"
    params = {
        'access_token': MAPBOX_API_KEY,
        'proximity': f"{lng},{lat}",
        'limit': limit
    }

    resp = requests.get(url, params=params)
    print(f"🔵 Mapbox Status: {resp.status_code}")
    
    if resp.status_code != 200:
        print("❌ Mapbox API failed.")
        return []

    data = resp.json()
    features = data.get('features', [])

    print(f"🟢 Found {len(features)} results.")

    places = []
    for feature in features:
        coords = feature.get('center', [None, None])
        places.append({
            'name': feature.get('text', 'Unnamed'),
            'address': feature.get('place_name', ''),
            'rating': None,  # Mapbox doesn't provide ratings
            'location': {
                'lat': coords[1],
                'lng': coords[0]
            }
        })

    return places
