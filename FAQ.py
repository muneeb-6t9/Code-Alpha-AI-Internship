import streamlit as st  # Web interface
import spacy  # NLP
from spacy.cli import download

# Ensure the SpaCy model is installed
model_name = "en_core_web_sm"

try:
    nlp = spacy.load(model_name)
except OSError:
    st.warning("Downloading the SpaCy model... Please wait.")
    download(model_name)  # Download model if not available
    nlp = spacy.load(model_name)  # Load again after download

# Define FAQs
faqs = [
    {"question": "What is your product?", "answer": "Our product is an AI-powered chatbot designed to assist users."},
    {"question": "How do I contact support?", "answer": "You can contact support via email at support@example.com."},
    {"question": "What is the refund policy?", "answer": "We offer a 30-day refund policy for unused products."},
    {"question": "Do you offer discounts?", "answer": "Yes, we offer discounts during special sales or for bulk purchases."},
]

def get_best_match(user_query):
    """Find the best matching FAQ question using NLP."""
    user_doc = nlp(user_query)
    best_match = None
    best_score = 0

    for faq in faqs:
        faq_doc = nlp(faq["question"])
        similarity = user_doc.similarity(faq_doc)
        if similarity > best_score:
            best_score = similarity
            best_match = faq

    return best_match, best_score

# Streamlit Web App
def main():
    st.title("🤖 FAQ Chatbot")
    st.write("Ask me any question about our product or services!")

    user_query = st.text_input("🔍 Type your question below:")

    if user_query:
        with st.spinner("Searching for the best answer..."):
            match, score = get_best_match(user_query)

        if match and score > 0.5:
            st.success(f"**Answer:** {match['answer']}")
            st.write(f"📊 (Confidence Score: {score:.2f})")
        else:
            st.warning("🚫 Sorry, I couldn't find an answer to your question. Please try rephrasing it.")

    st.markdown("---")
    st.write("⚡ **Powered by SpaCy & Streamlit.**")
    
if __name__ == "__main__":
    main()
