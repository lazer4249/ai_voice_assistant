import webbrowser
import datetime
from core.habit_learner import save_habit

from gtts import gTTS
import uuid
import os
from playsound import playsound

def speak(text):
    """Speak using gTTS + playsound, compatible with Streamlit."""
    try:
        print(f"[SPEAK] {text}")
        tts = gTTS(text=text, lang='en')
        filename = f"temp_{uuid.uuid4()}.mp3"
        tts.save(filename)
        playsound(filename)
        os.remove(filename)
    except Exception as e:
        print(f"[ERROR] Speaking failed: {e}")

def execute_intent(intent):
    """
    Executes a task based on the recognized intent.
    Logs each action as a habit using save_habit().
    """
    intent = intent.strip().lower()

    try:
        if intent == "open_browser":
            webbrowser.open("https://www.google.com")
            speak("Opening your browser.")
            save_habit("open_browser")

        elif intent == "tell_time":
            current_time = datetime.datetime.now().strftime("%I:%M %p")
            speak(f"The time is {current_time}.")
            save_habit("tell_time")

        elif intent == "set_reminder":
            speak("Your reminder has been set.")
            save_habit("set_reminder")

        elif intent == "greet":
            speak("Hello! How can I assist you today?")
            save_habit("greet")

        else:
            speak("Sorry, I didn't understand that command.")
            save_habit("unknown_intent")

    except Exception as e:
        print(f"[ERROR] Failed to execute intent '{intent}': {e}")
