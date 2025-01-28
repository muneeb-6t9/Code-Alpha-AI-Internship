import streamlit as st
from deep_translator import GoogleTranslator

# Title
st.title("Language Translation Tool")

# User input
text_to_translate = st.text_area("Enter text to translate:")

# Language options
languages = {
    "Afrikaans": "af", "Arabic": "ar", "Bengali": "bn", "Chinese": "zh-cn",
    "French": "fr", "German": "de", "Hindi": "hi", "Italian": "it",
    "Japanese": "ja", "Korean": "ko", "Portuguese": "pt", "Russian": "ru",
    "Spanish": "es", "Urdu": "ur",
}

target_language = st.selectbox("Select target language:", options=list(languages.keys()))

if st.button("Translate"):
    if text_to_translate.strip():
        try:
            translated_text = GoogleTranslator(source="auto", target=languages[target_language]).translate(text_to_translate)
            st.success(f"Translated Text ({target_language}):")
            st.write(translated_text)
        except Exception as e:
            st.error(f"Error: {e}")
    else:
        st.warning("Please enter some text to translate.")

