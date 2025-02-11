import streamlit as st  # For the web interface
import spacy  # For natural language processing

# Load the SpaCy English model
nlp = spacy.load("en_core_web_sm")

# Define FAQs as a list of questions and answers
faqs = [
    {"question": "What is your product?", "answer": "Our product is an AI-powered chatbot designed to assist users."},
    {"question": "How do I contact support?", "answer": "You can contact support via email at support@example.com."},
    {"question": "What is the refund policy?", "answer": "We offer a 30-day refund policy for unused products."},
    {"question": "Do you offer discounts?", "answer": "Yes, we offer discounts during special sales or for bulk purchases."},
]

def get_best_match(user_query):
    """
    This function takes the user's query and matches it to the most relevant FAQ question
    using SpaCy's similarity function.
    """
    user_doc = nlp(user_query)  # Process user query using SpaCy
    best_match = None
    best_score = 0  # Track the highest similarity score

    # Iterate through FAQs and calculate similarity scores
    for faq in faqs:
        faq_doc = nlp(faq["question"])  # Process FAQ question
        similarity = user_doc.similarity(faq_doc)  # Compute similarity between query and FAQ
        if similarity > best_score:  # Update best match if this one is better
            best_score = similarity
            best_match = faq

    return best_match, best_score


# Streamlit Web App
def main():
    st.title("FAQ Chatbot")  # App title
    st.write("Ask me any question about our product or services!")  # App description

    # User input field
    user_query = st.text_input("Type your question below:")

    # Check if the user has entered a question
    if user_query:
        # Get the best matching FAQ
        match, score = get_best_match(user_query)

        if match and score > 0.5:  # If a good match is found
            st.success(f"**Answer:** {match['answer']}")
            st.write(f"(Confidence Score: {score:.2f})")
        else:  # If no good match is found
            st.warning("Sorry, I couldn't find an answer to your question. Please try rephrasing it.")

    # Footer
    st.write("Powered by SpaCy and Streamlit. Enjoy your AI experience!")


if __name__ == "__main__":
    main()
