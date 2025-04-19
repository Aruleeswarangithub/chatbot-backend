# nlu/entity_extractor.py

def extract_place_type(user_input):
    print(f"🟣 Received user input: {user_input}")
    # Normalize input to lowercase
    text = user_input.lower()
    
    # Handle common plurals by simple replacement
    text = text.replace('rest stops', 'rest stop')
    text = text.replace('shops', 'shop')
    text = text.replace('stores', 'store')

    place_keywords = {
        "restaurant": "restaurant",
        "cafe": "cafe",
        "hotel": "lodging",
        "fuel": "gas_station",
        "gas": "gas_station",
        "parking": "parking",
        "hospital": "hospital",
        "mechanic": "car_repair",
        "charging": "charging_station",
        "rest stop": "rest_stop",
        "toilet": "toilet",
        "washroom": "toilet",
        "shop": "store",
        "store": "store"
    }

    # Debug logging
    print(f"🟣 extract_place_type received: '{user_input}', normalized: '{text}'")

    for keyword, place_type in place_keywords.items():
        if keyword in text:
            print(f"🔵 Matched keyword: '{keyword}', returning type: '{place_type}'")
            return place_type

    # Default to 'store' if nothing matches
    print("🔴 No keyword matched; defaulting to 'store'")
    return "store"  # default
