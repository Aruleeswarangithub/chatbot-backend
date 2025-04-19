from flask import Blueprint, request, jsonify
from places_service import get_places_nearby
from nlu.intent_classifier import classify_intent
from nlu.entity_extractor import extract_place_type

places_bp = Blueprint('places', __name__)

@places_bp.route('/api/query', methods=['POST'])
def handle_query():
    data = request.json
    user_input = data.get("query")
    location = data.get("location")  # "lat,lng"

    # Log incoming query and location
    print(f"🟡 Query: {user_input}")
    print(f"📍 Location: {location}")

    # Classify intent
    intent = classify_intent(user_input)
    print(f"🟢 Intent: {intent}")

    if intent == "location":
        # Extract place type and log
        place_type = extract_place_type(user_input) or "restaurant"
        print(f"🔍 Place Type: {place_type}")
        
        places = get_places_nearby(location, place_type)
        return jsonify({"response_type": "places", "places": places, "intent": intent})
    elif intent == "weather":
        # Forward to weather handler (not implemented in this route)
        return jsonify({"response_type": "weather", "intent": intent})
    else:
        # Default response if intent doesn't match
        return jsonify({"response_type": "chat", "text": "Hello! How can I assist you today?", "intent": intent})
