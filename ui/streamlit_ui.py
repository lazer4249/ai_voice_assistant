import streamlit as st
from core.habit_learner import get_daily_summary
from core.tts_engine import speak
import pandas as pd

def render_ui():
    st.title("AI Voice Assistant - Daily Habit Learner")
    summary = get_daily_summary()

    st.subheader("Today's Activities:")
    if summary:
        st.table(pd.DataFrame(summary, columns=["Habit"]))
    else:
        st.write("No activities recorded today.")

    if st.button("Speak Summary"):
        full_summary = "You did the following today: " + ", ".join(summary) if summary else "No habits found today."
        speak(full_summary)
