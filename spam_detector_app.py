
import streamlit as st
import pickle
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from nltk.tokenize import word_tokenize
import pandas as pd

# Download NLTK data (run once)
try:
    nltk.data.find('tokenizers/punkt')
    nltk.data.find('corpora/stopwords')
except LookupError:
    nltk.download('punkt')
    nltk.download('stopwords')

# Initialize stemmer
ps = PorterStemmer()

def preprocess_text(text):
    """
    Preprocess text for NLP tasks
    """
    # Convert to lowercase
    text = text.lower()

    # Remove special characters and digits
    text = re.sub('[^a-zA-Z]', ' ', text)

    # Tokenize
    tokens = word_tokenize(text)

    # Remove stopwords and apply stemming
    stop_words = set(stopwords.words('english'))
    tokens = [ps.stem(word) for word in tokens if word not in stop_words and len(word) > 2]

    return ' '.join(tokens)

@st.cache_resource
def load_models():
    """Load the trained model and vectorizer"""
    try:
        with open('best_spam_model.pkl', 'rb') as f:
            model = pickle.load(f)
        with open('tfidf_vectorizer.pkl', 'rb') as f:
            vectorizer = pickle.load(f)
        return model, vectorizer
    except FileNotFoundError:
        st.error("Model files not found! Please run the training notebook first.")
        return None, None

def predict_spam(text, model, vectorizer):
    """
    Predict if a text message is spam or ham
    """
    if model is None or vectorizer is None:
        return None

    # Preprocess the text
    processed_text = preprocess_text(text)

    # Vectorize
    text_vector = vectorizer.transform([processed_text]).toarray()

    # Predict
    prediction = model.predict(text_vector)[0]
    probability = model.predict_proba(text_vector)[0]

    return {
        'prediction': 'Spam' if prediction == 1 else 'Ham',
        'confidence': max(probability),
        'spam_probability': probability[1],
        'ham_probability': probability[0]
    }

# Streamlit App
def main():
    st.set_page_config(
        page_title="SMS Spam Detection",
        page_icon="📱",
        layout="wide"
    )

    st.title("📱 SMS Spam Detection System")
    st.write("Enter a text message to check if it's spam or ham (legitimate message)")

    # Load models
    model, vectorizer = load_models()

    if model is not None and vectorizer is not None:
        # Create two columns
        col1, col2 = st.columns([2, 1])

        with col1:
            # Text input
            user_input = st.text_area(
                "Enter your message:",
                height=150,
                placeholder="Type your message here..."
            )

            # Example messages
            st.subheader("Try these examples:")
            examples = [
                "Congratulations! You've won a £1000 cash prize! Call now!",
                "Hey, are we still meeting for lunch tomorrow?",
                "FREE! Click here to claim your prize now!",
                "Can you pick up some milk on your way home?",
                "URGENT! Your account will be suspended. Click link to verify!"
            ]

            for i, example in enumerate(examples):
                if st.button(f"Example {i+1}: {example[:50]}...", key=f"example_{i}"):
                    user_input = example
                    st.experimental_rerun()

        with col2:
            st.subheader("Results")

            if user_input:
                # Make prediction
                result = predict_spam(user_input, model, vectorizer)

                if result:
                    # Display results
                    if result['prediction'] == 'Spam':
                        st.error(f"🚨 **{result['prediction']}**")
                        st.write(f"Confidence: {result['confidence']:.1%}")
                    else:
                        st.success(f"✅ **{result['prediction']}**")
                        st.write(f"Confidence: {result['confidence']:.1%}")

                    # Probability breakdown
                    st.subheader("Probability Breakdown")
                    st.write(f"Ham: {result['ham_probability']:.1%}")
                    st.write(f"Spam: {result['spam_probability']:.1%}")

                    # Progress bars
                    st.progress(result['ham_probability'])
                    st.progress(result['spam_probability'])
            else:
                st.info("Enter a message above to get started!")

        # Model information
        st.sidebar.title("Model Information")
        st.sidebar.info(
            """
            This spam detection system uses advanced machine learning to classify SMS messages.
            
            **Features:**
            - Text preprocessing with stemming
            - TF-IDF vectorization
            - 11 ML models tested and compared
            - Extended Naive Bayes analysis
            - Real-time prediction
            
            **Dataset:** SMS Spam Collection Dataset (5,169 messages)
            **Best Model:** Random Forest Classifier
            """
        )
        
        # Updated Statistics from comprehensive analysis
        st.sidebar.subheader("Model Performance")
        st.sidebar.metric("Best Accuracy", "97.87%", "Random Forest")
        st.sidebar.metric("Best F1-Score", "91.25%", "Multinomial NB")
        st.sidebar.metric("Models Tested", "11", "6 Original + 5 NB Variants")
        
        # Model comparison summary
        st.sidebar.subheader("Top 3 Models")
        st.sidebar.write("🥇 Multinomial NB (Count): 91.25% F1")
        st.sidebar.write("🥈 Random Forest: 90.91% F1") 
        st.sidebar.write("🥉 Bernoulli NB (TF-IDF): 90.91% F1")
        
    else:
        st.error("Please run the training notebook first to generate the model files.")

if __name__ == "__main__":
    main()
