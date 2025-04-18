# backend/app.py
from flask import Flask, request, jsonify
from dotenv import load_dotenv
import os

from nlu.intent_classifier import classify_intent
from nlu.entity_extractor import extract_place_type
from places_service import get_places_nearby

# load environment variables from .env
load_dotenv()

app = Flask(__name__)

@app.route('/api/query', methods=['POST'])
def handle_query():
    data = request.get_json()
    user_input = data.get('query')
    location = data.get('location')  # expected format: "lat,lng"

    if not user_input or not location:
        return jsonify({'error': 'Missing query or location'}), 400

    intent = classify_intent(user_input)

    if intent == 'location':
        place_type = extract_place_type(user_input)
        places = get_places_nearby(location, place_type)
        return jsonify({'response_type': 'places', 'places': places})
    elif intent == 'weather':
        # TODO: integrate weather_service
        return jsonify({'response_type': 'weather', 'text': 'Weather feature coming soon.'})
    else:
        return jsonify({'response_type': 'chat', 'text': "Sorry, I didn't understand that."})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
