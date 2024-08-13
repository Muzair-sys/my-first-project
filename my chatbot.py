import streamlit as st
import google.generativeai as genai

API_KEY = "AIzaSyA7IzBS4cqt3xGsOKmxOYz8JGZ0pTPTpsI"
genai.configure(api_key=API_KEY)

# Initialize the model
model = genai.GenerativeModel('gemini-1.5-flash')

def getResponseFromModel(user_input):
    response = model.generate_content(user_input)
    return response.text

# Streamlit app title
st.title("Gemini Chatbot")

# Streamlit input for user prompt
user_input = st.text_input("Enter Your Prompt:")

# Streamlit button to get the response
if st.button("Get Response"):
    if user_input:
        output = getResponseFromModel(user_input)
        st.write(f"Chat Response: {output}")
    else:
        st.write("Please enter a prompt.")
