import streamlit as st
from openai import OpenAI
import os

st.title("💬 Chatbot")

#  API key from .streamlit/secrets.toml
api_key = st.secrets.get("OPENROUTER_API_KEY")

# Error if no key found
if not api_key:
    st.error("Brak klucza API! Dodaj OPENROUTER_API_KEY do .streamlit/secrets.toml")
    st.stop()

# OpenAI client initialization with OpenRouter 
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=api_key,
)

# List of available models
model = st.selectbox("Wybierz model", [
    "openai/gpt-3.5-turbo",
    "openai/gpt-4",
    "mistralai/mistral-7b-instruct",
    "meta-llama/llama-3.3-8b-instruct:free",
])

# User's message
user_input = st.text_area("🧑‍💻 Twoje pytanie:", height=100)

# When the user clicks "Wyślij"
if st.button("Wyślij"):
    if not user_input.strip():
        st.warning("Wpisz coś, zanim wyślesz!")
    else:
        with st.spinner("Czekam na odpowiedź..."):
            try:
                response = client.chat.completions.create(
                    model=model,
                    messages=[
                        {"role": "user", "content": user_input}
                    ],
                    extra_headers={
                        "HTTP-Referer": "https://github.com/twoj-login/streamlit-llm-app",  # Opcjonalne
                        "X-Title": "Streamlit Chatbot App",  # Opcjonalne
                    }
                )
                st.markdown("### 🤖 Odpowiedź:")
                st.write(response.choices[0].message.content)

            except Exception as e:
                st.error(f"❌ Błąd: {e}")
