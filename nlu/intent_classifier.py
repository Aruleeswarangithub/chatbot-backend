# nlu/intent_classifier.py

def classify_intent(user_input):
    user_input = user_input.lower()

    if any(keyword in user_input for keyword in ["weather", "temperature", "rain", "forecast"]):
        return "weather"
    elif any(keyword in user_input for keyword in [
        "hospital", "fuel", "gas", "restaurant", "cafe", "hotel", "parking",
        "mechanic", "charging", "rest stop", "toilet", "washroom"
    ]):
        return "location"
    else:
        return "smalltalk"
