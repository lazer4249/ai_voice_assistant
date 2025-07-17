import streamlit as st
from core.speech_processor import listen_command
from core.intent_handler import get_intent
from core.action_executor import execute_intent
from core.habit_learner import get_daily_summary
import pandas as pd

def main():
    st.title("🧠 AI Voice Assistant - Daily Habit Learner")

    # Show today's summary table
    st.subheader("📋 Today's Habits:")
    summary = get_daily_summary()
    if summary:
        st.table(pd.DataFrame(summary, columns=["Habit"]))
    else:
        st.write("No activities recorded today.")

    if st.button("🎙️ Start Listening"):
        st.info("Listening... Please say a command.")
        command = listen_command()

        if command:
            st.success(f"Recognized Speech: `{command}`")
            intent = get_intent(command)
            st.success(f"✅ Recognized Intent: `{intent}`")
            execute_intent(intent)
        else:
            st.error("❌ Could not understand audio. Please try again.")

if __name__ == "__main__":
    main()
