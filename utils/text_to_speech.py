# utils/text_to_speech.py

import pyttsx3

def speak(text: str, language: str = 'en'):
    """Convert text to speech and speak it aloud."""
    
    # Initialize the speech engine
    engine = pyttsx3.init()

    # Set the language (you can set different languages based on your requirement)
    voices = engine.getProperty('voices')
    
    # Setting the default voice to English (you can change it to other voices as needed)
    if language == 'en':
        engine.setProperty('voice', voices[1].id)  # English (Male) voice
    elif language == 'ta':
        engine.setProperty('voice', voices[2].id)  # Tamil voice (may need to adjust for the specific language)

    # Set the speech rate (speed)
    engine.setProperty('rate', 150)

    # Set the volume (0.0 to 1.0)
    engine.setProperty('volume', 1.0)

    # Speak the text
    engine.say(text)
    engine.runAndWait()

