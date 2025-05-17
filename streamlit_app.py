import streamlit as st
from openai import OpenAI
import os
import fitz

st.title("💬 Chatbot z PDF")

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

# Upload PDF
st.markdown("---")
st.subheader("📄 Załaduj plik PDF")

uploaded_file = st.file_uploader("Wybierz plik PDF", type="pdf")
pdf_text = ""

if uploaded_file is not None:
    with st.spinner("Wydobywanie tekstu z PDF..."):
        try:
            doc = fitz.open(stream=uploaded_file.read(), filetype="pdf")
            pdf_text = "\n".join([page.get_text() for page in doc])
            st.success("Tekst został wydobyty!")
            st.text_area("📄 Podgląd treści PDF", pdf_text[:3000], height=200)
        except Exception as e:
            st.error(f"Błąd podczas odczytu PDF: {e}")

# User question
st.markdown("---")
st.subheader("🧑‍💻 Zapytaj model na podstawie dokumentu")
user_input = st.text_area("Twoje pytanie:", height=100)

if st.button("Wyślij"):
    if not user_input.strip():
        st.warning("Wpisz pytanie przed wysłaniem.")
    elif not pdf_text:
        st.warning("Najpierw załaduj plik PDF.")
    else:
        with st.spinner("Czekam na odpowiedź..."):
            try:
                response = client.chat.completions.create(
                    model=model,
                    messages=[
                        {"role": "system", "content": "Jesteś pomocnym asystentem, który odpowiada na pytania na podstawie dostarczonego dokumentu PDF."},
                        {"role": "user", "content": f"Oto zawartość dokumentu:\n{pdf_text[:4000]}\n\nPytanie: {user_input}"}
                    ],
                    extra_headers={
                        "HTTP-Referer": "https://github.com/twoj-login/streamlit-llm-app",
                        "X-Title": "Streamlit PDF Chatbot"
                    }
                )
                st.markdown("### 🤖 Odpowiedź:")
                st.write(response.choices[0].message.content)
            except Exception as e:
                st.error(f"❌ Błąd podczas zapytania: {e}")
