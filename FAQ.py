import streamlit as st
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Define FAQs
faqs = [
    {"question": "What is your product?", "answer": "Our product is an AI-powered chatbot designed to assist users."},
    {"question": "How do I contact support?", "answer": "You can contact support via email at support@example.com."},
    {"question": "What is the refund policy?", "answer": "We offer a 30-day refund policy for unused products."},
    {"question": "Do you offer discounts?", "answer": "Yes, we offer discounts during special sales or for bulk purchases."},
]

# Extract just the FAQ questions for vectorization
faq_questions = [faq["question"] for faq in faqs]

# TF-IDF Vectorizer (turns text into numerical data)
vectorizer = TfidfVectorizer()
faq_vectors = vectorizer.fit_transform(faq_questions)  # Convert FAQ questions to vectors


def get_best_match(user_query):
    """Finds the best matching FAQ question using TF-IDF and cosine similarity."""
    user_vector = vectorizer.transform([user_query])  # Convert user query to vector
    similarities = cosine_similarity(user_vector, faq_vectors)[0]  # Compute similarity scores

    best_index = similarities.argmax()  # Find highest similarity score
    best_score = similarities[best_index]

    if best_score > 0.5:  # Set a similarity threshold
        return faqs[best_index], best_score
    return None, best_score


# Streamlit Web App
def main():
    st.title("🤖 FAQ Chatbot </br>(Code-Alpha-Internship)")
    st.write("Ask me any question about our product or services!")

    user_query = st.text_input("🔍 Type your question below:")

    if user_query:
        match, score = get_best_match(user_query)
        if match:
            st.success(f"**Answer:** {match['answer']}")
            st.write(f"_(Confidence Score: {score:.2f})_")
        else:
            st.warning("Sorry, I couldn't find an answer. Please try rephrasing.")

    st.write("📌 **Powered by TF-IDF & Streamlit**")


if __name__ == "__main__":
    main()
