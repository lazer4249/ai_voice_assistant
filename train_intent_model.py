import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
import joblib
import os

# Load data
df = pd.read_csv("data/intent_dataset.csv")

# Define pipeline
pipeline = Pipeline([
    ('vectorizer', TfidfVectorizer()),
    ('classifier', LogisticRegression())
])

# Train
pipeline.fit(df['text'], df['intent'])

# Save model and vectorizer
os.makedirs("models", exist_ok=True)
joblib.dump(pipeline, "models/nlp_model.pkl")
print("Model trained and saved!")
