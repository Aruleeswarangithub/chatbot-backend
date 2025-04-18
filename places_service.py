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
    params = {
        'location': location,
        'radius': radius,
        'type': place_type,
        'key': GOOGLE_API_KEY
    }
    resp = requests.get(GOOGLE_PLACES_URL, params=params)
    
    # Log HTTP status and response status
    print(f"HTTP Status: {resp.status_code}")
    data = resp.json()
    print(f"API Response Status: {data.get('status')}")
    
    if resp.status_code != 200 or data.get('status') != 'OK':
        print("Error: Failed to retrieve places.")
        return []
    
    results = data.get('results', [])
    
    # Log a sample of the results
    if results:
        print(f"Sample of Results: {results[0]}")

    # Sort results by rating (descending)
    results.sort(key=lambda x: x.get('rating', 0), reverse=True)

    # Simplify the response
    places = []
    for place in results:
        places.append({
            'name': place.get('name'),
            'address': place.get('vicinity'),
            'rating': place.get('rating', 0),
            'location': place.get('geometry', {}).get('location')
        })
    
    return places
