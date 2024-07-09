import streamlit as st
import requests
import json

st.title("Interactive Assistant")

message = st.text_area("Enter your message:")

if st.button("Send"):
    with st.spinner("Processing..."):
        response = requests.post(
            'https://chatbot-api-assistant-sam318.replit.app/send_message',
            json={"message": message}
        )

        if response.status_code == 200:
            data = response.json()
            st.text_area("Response:", value=data['response'], height=300)
        else:
            st.error("Error: Unable to get the response.")
