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

    # Debug logging to track the incoming query and location
    print(f"🟡 User Input: {user_input}")
    print(f"🟢 Location: {location}")

    intent = classify_intent(user_input)

    # Log the intent classification
    print(f"🔵 Intent: {intent}")

    if intent == "location":
        place_type = extract_place_type(user_input)

        # Log the extracted place type
        print(f"🟣 Extracted Place Type: {place_type}")

        places = get_places_nearby(location, place_type)

        # Log the places found
        print(f"🟠 Places Found: {places}")

        return jsonify({
            "response_type": "places",
            "places": places,
            "intent": intent
        })

    elif intent == "weather":
        # Log the weather intent handling
        print("🌤️ Weather Intent Received")

        # Forward to your weather handler if necessary
        return jsonify({
            "response_type": "weather",
            "intent": intent
        })

    else:
        # Log the fallback response
        print("💬 Fallback Chat Response")

        return jsonify({
            "response_type": "chat",
            "text": "Hello! How can I assist you today?",
            "intent": intent
        })
