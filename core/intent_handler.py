import joblib

# Load trained pipeline (which includes vectorizer and classifier)
model = joblib.load("models/nlp_model.pkl")

def get_intent(text):
    text = text.strip().lower()  # Normalize input
    return model.predict([text])[0]
