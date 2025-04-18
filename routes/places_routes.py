# routes/places_routes.py

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

    intent = classify_intent(user_input)

    if intent == "location":
        place_type = extract_place_type(user_input)
        places = get_places_nearby(location, place_type)
        return jsonify({"response_type": "places", "places": places, "intent": intent})
    elif intent == "weather":
        # Forward to weather handler
        return jsonify({"response_type": "weather", "intent": intent})
    else:
        return jsonify({"response_type": "chat", "text": "Hello! How can I assist you today?", "intent": intent})
