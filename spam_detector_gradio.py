
import gradio as gr
import pickle
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from nltk.tokenize import word_tokenize

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
    """Preprocess text for NLP tasks"""
    text = text.lower()
    text = re.sub('[^a-zA-Z]', ' ', text)
    tokens = word_tokenize(text)
    stop_words = set(stopwords.words('english'))
    tokens = [ps.stem(word) for word in tokens if word not in stop_words and len(word) > 2]
    return ' '.join(tokens)

# Load models
try:
    with open('best_spam_model.pkl', 'rb') as f:
        model = pickle.load(f)
    with open('tfidf_vectorizer.pkl', 'rb') as f:
        vectorizer = pickle.load(f)
    models_loaded = True
except FileNotFoundError:
    models_loaded = False
    print("Model files not found! Please run the training notebook first.")

def predict_message(text):
    """Predict if a message is spam or ham"""
    if not models_loaded:
        return "Error: Models not loaded", 0.0, 0.0, 0.0

    if not text.strip():
        return "Please enter a message", 0.0, 0.0, 0.0

    # Preprocess and predict
    processed_text = preprocess_text(text)
    text_vector = vectorizer.transform([processed_text]).toarray()
    prediction = model.predict(text_vector)[0]
    probabilities = model.predict_proba(text_vector)[0]

    result = "🚨 SPAM" if prediction == 1 else "✅ HAM (Safe)"
    confidence = max(probabilities)
    spam_prob = probabilities[1]
    ham_prob = probabilities[0]

    return result, confidence, ham_prob, spam_prob

# Example messages
examples = [
    ["Congratulations! You've won a £1000 cash prize! Call now to claim your reward!"],
    ["Hey, are we still meeting for lunch tomorrow?"],
    ["FREE! Click here to claim your prize now! Limited time offer!"],
    ["Can you pick up some milk on your way home?"],
    ["URGENT! Your account will be suspended. Click link to verify immediately!"]
]

# Create Gradio interface
with gr.Blocks(title="SMS Spam Detection", theme=gr.themes.Soft()) as interface:
    gr.Markdown("# 📱 SMS Spam Detection System")
    gr.Markdown("""
    **Advanced spam detection using 11 machine learning models**
    
    🏆 **Best Results:**
    - 🥇 Multinomial NB (Count): 91.25% F1-Score
    - 🥈 Random Forest: 90.91% F1-Score  
    - 🥉 Bernoulli NB (TF-IDF): 90.91% F1-Score
    
    📊 **Dataset:** 5,169 SMS messages | **Models Tested:** 11 (6 Original + 5 NB Variants)
    """)
    
    with gr.Row():
        with gr.Column(scale=2):
            text_input = gr.Textbox(
                label="Enter your message:",
                placeholder="Type your message here...",
                lines=3
            )
            
            predict_button = gr.Button("🔍 Analyze Message", variant="primary")
            
        with gr.Column(scale=1):
            result_output = gr.Textbox(label="Prediction", interactive=False)
            confidence_output = gr.Number(label="Confidence", precision=3)
            
            with gr.Row():
                ham_prob = gr.Number(label="Ham Probability", precision=3)
                spam_prob = gr.Number(label="Spam Probability", precision=3)
                gr.Markdown("### Try these examples:")
    gr.Examples(
        examples=examples,
        inputs=[text_input],
        outputs=[result_output, confidence_output, ham_prob, spam_prob],
        fn=predict_message
    )

    predict_button.click(
        fn=predict_message,
        inputs=[text_input],
        outputs=[result_output, confidence_output, ham_prob, spam_prob]
    )

if __name__ == "__main__":
    interface.launch(share=True, debug=True)
