# backend/places_service.py

import requests
from config import GOOGLE_API_KEY

GOOGLE_PLACES_URL = "https://maps.googleapis.com/maps/api/place/nearbysearch/json"

def get_places_nearby(location, place_type, radius=5000):
    """
    Query Google Places API for nearby locations sorted by rating.

    Args:
        location (str): "latitude,longitude"
        place_type (str): e.g., 'cafe', 'restaurant', 'gas_station'
        radius (int): search radius in meters

    Returns:
        List of dicts with keys: name, address, rating, location
    """
    # Debug: log inputs
    print(f"🔍 Searching places near {location} for type: {place_type} (radius={radius}m)")

    params = {
        'location': location,
        'radius': radius,
        'type': place_type,
        'key': GOOGLE_API_KEY
    }
    resp = requests.get(GOOGLE_PLACES_URL, params=params)

    # Parse JSON and log status
    data = resp.json()
    print(f"🟢 HTTP Status Code: {resp.status_code}")
    print(f"🟢 Google API Status: {data.get('status')}")
    print(f"🟢 Sample Results: {data.get('results')[:3]}")  # show up to first 3 results

    # If something went wrong, return empty
    if resp.status_code != 200 or data.get('status') != 'OK':
        return []

    results = data.get('results', [])
    # sort by rating descending
    results.sort(key=lambda x: x.get('rating', 0), reverse=True)

    # Simplify the response structure
    places = []
    for place in results:
        places.append({
            'name': place.get('name'),
            'address': place.get('vicinity'),
            'rating': place.get('rating', 0),
            'location': place.get('geometry', {}).get('location')
        })

    # Debug: log final simplified places
    print(f"🟣 Simplified places list (count={len(places)}): {places[:3]}")

    return places
