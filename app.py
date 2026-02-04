import streamlit as st
import pickle
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

model_path = os.path.join(BASE_DIR, "model", "sentiment_model.pkl")
vectorizer_path = os.path.join(BASE_DIR, "model", "tfidf_vectorizer.pkl")

model = pickle.load(open(model_path, "rb"))
tfidf = pickle.load(open(vectorizer_path, "rb"))


st.title("Flipkart Review Sentiment Analysis")

review = st.text_area("Enter your review")

if st.button("Predict Sentiment"):
    if review.strip() == "":
        st.warning("Please enter a review")
    else:
        review_vec = tfidf.transform([review])
        pred = model.predict(review_vec)[0]

        if pred == 1:
            st.success("😊 Positive Review")
        else:
            st.error("☹️ Negative Review")
