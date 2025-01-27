import streamlit as st
from googletrans import Translator

# Initialize translator
translator = Translator()

# Title of the app
st.title("Language Translation Tool")

# Input: Text to translate
text_to_translate = st.text_area("Enter text to translate:", placeholder="Type your text here...")

# Input: Choose target language
languages = {
    "Afrikaans": "af", "Arabic": "ar", "Bengali": "bn", "Chinese": "zh-cn",
    "French": "fr", "German": "de", "Hindi": "hi", "Italian": "it",
    "Japanese": "ja", "Korean": "ko", "Portuguese": "pt", "Russian": "ru",
    "Spanish": "es", "Urdu": "ur",
}
target_language = st.selectbox("Select target language:", options=list(languages.keys()))

# Translate button
if st.button("Translate"):
    if text_to_translate.strip():
        try:
            # Perform translation
            translated = translator.translate(text_to_translate, dest=languages[target_language])
            st.success(f"Translated Text ({target_language}):")
            st.write(translated.text)
        except Exception as e:
            st.error(f"An error occurred during translation: {e}")
    else:
        st.warning("Please enter some text to translate.")

# Footer
st.write("Powered by [Google Translate](https://cloud.google.com/translate)")
