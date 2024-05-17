from dotenv import load_dotenv
load_dotenv() ### loading the environment variables
import os
import streamlit as st
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

### function to load the gemini pro model and get responses
model = genai.GenerativeModel("gemini-pro")
def getGeminiResponse(question):
    response = model.generate_content(question)
    return response.text

### initialize streamlit app

st.set_page_config(page_title="Q&A Application")
st.header("LARGE LANGUAGE MODEL APPLICATION")

input = st.text_input("Your Question: ", key="input")
submit = st.button("Submit")

if submit:
    response = getGeminiResponse(input)
    st.subheader("Response")
    st.write(response)