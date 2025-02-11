import streamlit as st
from deep_translator import GoogleTranslator

# Create an instance of GoogleTranslator
translotor=GoogleTranslator()

# Title
st.title("Language Translation Tool")

# User input
text_to_translate = st.text_area("Enter text to translate:")

# Language options
supported_languages = translotor.get_supported_languages()

language_codes = {lang.capitalize(): lang for lang in supported_languages}



target_language = st.selectbox("Select target language:", options=list(language_codes.keys()))

if st.button("Translate"):
    if text_to_translate.strip():
        try:
            translated_text = GoogleTranslator(source="auto", target=language_codes[target_language]).translate(text_to_translate)
            st.success(f"Translated Text ({target_language}):")
            st.write(translated_text)
        except Exception as e:
            st.error(f"Error: {e}")
    else:
        st.warning("Please enter some text to translate.")


