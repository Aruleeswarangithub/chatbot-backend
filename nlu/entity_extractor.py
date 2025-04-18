# nlu/entity_extractor.py

def extract_place_type(user_input):
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

    for keyword, place_type in place_keywords.items():
        if keyword in user_input.lower():
            return place_type
    return "store"  # default
