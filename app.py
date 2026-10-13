from pathlib import Path

import streamlit as st
import joblib

st.set_page_config(page_title="AI Customer Feedback Analyzer")

MODEL_PATH = Path(__file__).resolve().parent / "sentiment_model.pkl"


@st.cache_resource
def load_model():
    return joblib.load(MODEL_PATH)


st.title("🤖 AI Customer Feedback Analyzer")
st.write("Enter a customer review below and click Analyze.")

if not MODEL_PATH.is_file():
    st.error(
        "The trained model is missing. Run `python save_model.py` from the "
        "project folder to create it."
    )
    st.stop()

model = load_model()

# Input
review = st.text_area("Customer Review")

# Prediction
if st.button("Analyze"):
    if review.strip() == "":
        st.warning("Please enter a review.")
    else:
        prediction = model.predict([review])[0]

        if prediction == "Positive":
            st.success("😊 Sentiment: Positive")
        elif prediction == "Negative":
            st.error("😞 Sentiment: Negative")
        else:
            st.info("😐 Sentiment: Neutral")