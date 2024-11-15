import streamlit as st
import requests

# Set title
st.title("Emotion Detection App")

text = st.text_input("Input text:")
is_clicked = st.button("Predict emotion")

col1, col2 = st.columns(2)

if is_clicked:
  response = requests.post(url="http://127.0.0.1:8000/predict", json={"text": text})

  if response.status_code == 200:
    prediction = response.json()
    col1.metric(label=f"Emotion:", value=prediction['emotion'].capitalize())
    col2.metric(f"Confidence score:", value=f"{prediction['confidence']:.2f}")
  else:
    st.error("Inference failed!")

