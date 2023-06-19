import streamlit as st
import requests
import json

CONFIG_PATH = "/app/config.json"
API_URL = "https://api.openai.com/v1/chat/completions"

def get_api_key():
    with open(CONFIG_PATH) as config_file:
        config_data = json.load(config_file)
        return config_data["api_key"]

def save_api_key(api_key):
    with open(CONFIG_PATH, "w") as config_file:
        json.dump({"api_key": api_key}, config_file)

def call_chatgpt_api(prompt):
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {get_api_key()}"
    }
    data = {
        "prompt": prompt,
        "max_tokens": 50
    }
    response = requests.post(API_URL, json=data, headers=headers)
    response.raise_for_status()
    return response.json()["choices"][0]["text"].strip()

def main():
    st.title("ChatGPT Web Application")
    st.write("Welcome to the ChatGPT web application!")

    page = st.sidebar.radio("Navigation", ["Set API Key", "Chat"])

    if page == "Set API Key":
        st.header("Set API Key")
        api_key = st.text_input("API Key", get_api_key())
        if st.button("Save API Key"):
            save_api_key(api_key)
            st.success("API Key saved successfully.")

    elif page == "Chat":
        st.header("Chat with ChatGPT")
        user_input = st.text_input("User Input", "")
        response = st.text_area("ChatGPT Response", "")

        if st.button("Send"):
            response += f"You: {user_input}\n"
            chatgpt_response = call_chatgpt_api(user_input)
            response += f"ChatGPT: {chatgpt_response}\n"
            st.text_area("ChatGPT Response", response)

if __name__ == "__main__":
    main()
