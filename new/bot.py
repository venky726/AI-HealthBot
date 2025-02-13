import streamlit as st
import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables from .env file
load_dotenv()
gemini_api_key = os.getenv("GOOGLE_API_KEY")
if not gemini_api_key:
    st.error("Gemini API key not found. Please set GOOGLE_API_KEY in your .env file.")
    st.stop()

# Configure Gemini API with your key
try:
    genai.configure(api_key=gemini_api_key)
except Exception as e:
    st.error(f"Failed to configure Gemini API: {e}")
    st.stop()

# Initialize the Gemini model (use the appropriate model name, e.g., "gemini-pro")
try:
    model = genai.GenerativeModel("gemini-2.0-flash")  # Or your desired model
    chat = model.start_chat(history=[]) # Initialize chat history
except Exception as e:
    st.error(f"Failed to initialize Gemini model: {e}")
    st.stop()

st.title("AI HealthCare Assistant")

user_input = st.text_input("I'm here to assist you:")

if user_input:
    prompt = (
        "You are a helpful medical assistant. Provide concise and accurate medical information "
        "based on the user's query. Disclaimer: This information is for educational purposes only and is not a substitute for professional advice.\n\n"
        f"Question: {user_input}"
    )

    with st.spinner("Generating response..."): # Show a spinner while waiting for the response
        try:
            response = chat.send_message(prompt, stream=False)
            answer = response.text if response and hasattr(response, "text") else "Sorry, I could not generate a response."
            st.write(answer) # Display the answer
        except Exception as e:
            st.error(f"An error occurred: {e}") # Display any errors to the user