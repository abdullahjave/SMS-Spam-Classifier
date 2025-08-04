# 📱 SMS Spam Detection System

A comprehensive machine learning project for detecting spam messages using multiple algorithms and providing interactive web interfaces.

## 🎯 Project Overview

This project implements a complete SMS spam detection system with:
- **Data preprocessing and exploratory data analysis**
- **Multiple machine learning model comparison**
- **Interactive web interfaces (Streamlit & Gradio)**
- **High-performance spam classification**

## 📊 Results Summary

### 🏆 **Comprehensive Model Performance (11 Models Tested)**

#### **Top 5 Performing Models:**
1. **🥇 Multinomial NB (Count)**: 91.25% F1-Score | 97.78% Accuracy
2. **🥈 Random Forest**: 90.91% F1-Score | 97.87% Accuracy
3. **🥉 Bernoulli NB (TF-IDF)**: 90.91% F1-Score | 97.87% Accuracy
4. **4th Bernoulli NB (Binary)**: 90.91% F1-Score | 97.87% Accuracy
5. **5th SVM**: 90.61% F1-Score | 97.78% Accuracy

#### **Model Categories Tested:**
- **📊 Original Models**: 6 (Naive Bayes, Random Forest, SVM, Decision Tree, Logistic Regression, KNN)
- **🧠 Extended Naive Bayes**: 5 variants (Multinomial, Bernoulli, Gaussian with different vectorizers)

#### **Key Findings:**
- **Multinomial NB with Count Vectorizer** achieved the highest F1-score
- **Binary features** (Bernoulli NB) work excellently for spam detection
- **Gaussian NB** performed poorly (76.02% accuracy) for high-dimensional text data
- **Count-based features** outperformed TF-IDF for Multinomial NB
- **All models** significantly outperformed baseline approaches

### Dataset
- **Original size**: 5,572 messages
- **After cleaning**: 5,169 messages (403 duplicates removed)
- **Class distribution**: 87.4% Ham, 12.6% Spam
- **Features**: Text preprocessing with TF-IDF vectorization (3,000 features)

## 🚀 Features

### 📈 Comprehensive Analysis
- **Exploratory Data Analysis (EDA)** with visualizations
- **Extended Naive Bayes comparison** with 5 variants
- **Feature importance analysis** for best Multinomial NB
- **Confusion matrices** for top 3 models
- **Text length analysis** comparing spam vs ham messages
- **Word clouds** for spam and ham messages
- **Statistical analysis** of message characteristics

### 🤖 Machine Learning Models Tested (11 Total)

#### **Original Models (6):**
1. **Random Forest** (97.87% accuracy, 90.91% F1)
2. **Support Vector Machine** (97.78% accuracy, 90.61% F1)
3. **Naive Bayes** (96.91% accuracy, 86.32% F1)
4. **Decision Tree** (95.84% accuracy, 83.65% F1)
5. **Logistic Regression** (95.94% accuracy, 81.25% F1)
6. **K-Nearest Neighbors** (90.91% accuracy, 44.05% F1)

#### **Extended Naive Bayes Variants (5):**
1. **Multinomial NB (Count)** (97.78% accuracy, 91.25% F1) ⭐ **BEST F1**
2. **Bernoulli NB (TF-IDF)** (97.87% accuracy, 90.91% F1)
3. **Bernoulli NB (Binary)** (97.87% accuracy, 90.91% F1)
4. **Multinomial NB (TF-IDF)** (96.91% accuracy, 86.32% F1)
5. **Gaussian NB (TF-IDF)** (76.02% accuracy, 48.33% F1)

### 🌐 Interactive Web Interfaces
- **Streamlit App**: Feature-rich dashboard with detailed analytics
- **Gradio App**: Simple and clean interface for quick testing
- **Real-time prediction** with confidence scores
- **Example messages** for testing

### 🔧 Text Processing Pipeline
1. **Lowercase conversion**
2. **Special character removal**
3. **Tokenization** using NLTK
4. **Stopword removal**
5. **Stemming** with Porter Stemmer
6. **TF-IDF vectorization**

## 📁 Project Structure

```
spam-detection-system/
│
├── 📊 Data & Models
│   ├── spam.csv                     # Original dataset
│   ├── best_spam_model.pkl         # Trained Random Forest model
│   └── tfidf_vectorizer.pkl        # TF-IDF vectorizer
│
├── 📓 Analysis & Training
│   └── spam_system.ipynb           # Complete Jupyter notebook with EDA and training
│
├── 🌐 Web Applications
│   ├── spam_detector_app.py        # Streamlit application
│   ├── spam_detector_simple.py     # Simplified Streamlit app
│   ├── spam_detector_gradio.py     # Gradio application
│   ├── run_streamlit.py           # Streamlit launcher
│   └── run_gradio.py              # Gradio launcher
│
├── 📋 Documentation
│   ├── README.md                   # This file
│   ├── requirements.txt            # Python dependencies
│   └── RESULTS.md                  # Detailed results and analysis
│
└── 🚀 Setup Scripts
    └── setup.py                    # Installation script
```

## 🛠️ Installation & Setup

### Prerequisites
- Python 3.8+
- pip package manager

### Quick Setup
```bash
# Clone the repository
git clone https://github.com/yourusername/sms-spam-detection.git
cd sms-spam-detection

# Install dependencies
pip install -r requirements.txt

# Download NLTK data (run once)
python -c "import nltk; nltk.download('punkt'); nltk.download('stopwords')"
```

### Alternative Setup
```bash
# Use the setup script
python setup.py
```

## 🚀 Usage

### Option 1: Streamlit Web App (Recommended)
```bash
# Feature-rich dashboard
streamlit run spam_detector_app.py

# Or simplified version
streamlit run spam_detector_simple.py
```
- Opens at `http://localhost:8501`
- Full dashboard with model metrics
- Interactive examples and detailed results

### Option 2: Gradio Web App
```bash
python spam_detector_gradio.py
```
- Opens at `http://127.0.0.1:7860`
- Simple, clean interface
- Creates shareable public link

### Option 3: Jupyter Notebook
```bash
jupyter notebook spam_system.ipynb
```
- Complete analysis and training pipeline
- Detailed EDA and model comparisons
- Reproducible results

## 📊 Model Performance Details

### Confusion Matrix (Random Forest)
```
              Predicted
Actual    Ham    Spam
Ham       902     1
Spam       21   110
```

### Classification Report
```
              precision    recall  f1-score   support
         Ham       0.98      1.00      0.99       903
        Spam       0.99      0.84      0.91       131
    accuracy                           0.98      1034
   macro avg       0.98      0.92      0.95      1034
weighted avg       0.98      0.98      0.98      1034
```

### Key Insights from EDA
- **Spam messages** are generally longer (avg: 138 chars) than ham messages (avg: 70 chars)
- **Spam messages** contain more words on average (24 vs 14 words)
- **Common spam words**: "free", "call", "text", "claim", "win", "prize"
- **Common ham words**: "you", "will", "get", "now", "come", "time"

## 🧪 Testing Examples

### Spam Examples
```
"Congratulations! You've won a £1000 cash prize! Call now!"
"FREE! Click here to claim your prize now! Limited time offer!"
"URGENT! Your account will be suspended. Click link to verify!"
```

### Ham Examples
```
"Hey, are we still meeting for lunch tomorrow?"
"Can you pick up some milk on your way home?"
"Thanks for the help today, really appreciate it!"
```

## 🔬 Technical Implementation

### Data Preprocessing
- **Dataset**: SMS Spam Collection from UCI ML Repository
- **Cleaning**: Removed 403 duplicate messages
- **Encoding**: Label encoding (0=Ham, 1=Spam)
- **Text Processing**: NLTK-based preprocessing pipeline

### Feature Engineering
- **TF-IDF Vectorization** with 3,000 features
- **N-gram analysis** (unigrams)
- **Stopword removal** using NLTK English corpus
- **Stemming** using Porter Stemmer

### Model Selection
- **Cross-validation** for model evaluation
- **Stratified sampling** to maintain class distribution
- **Performance metrics**: Accuracy, Precision, Recall, F1-Score
- **Training time** and **prediction time** analysis

## 📈 Performance Metrics

| Model | Accuracy | Precision | Recall | F1-Score | Training Time |
|-------|----------|-----------|--------|----------|---------------|
| Random Forest | 97.87% | 99.10% | 83.97% | 90.91% | 34.6s |
| SVM | 97.78% | 97.37% | 84.73% | 90.61% | 12.9s |
| Naive Bayes | 96.91% | 98.06% | 77.10% | 86.32% | 0.1s |
| Decision Tree | 95.84% | 83.33% | 83.97% | 83.65% | 39.6s |
| Logistic Regression | 95.94% | 97.85% | 69.47% | 81.25% | 0.8s |
| K-Nearest Neighbors | 90.91% | 100.00% | 28.24% | 44.05% | 0.03s |

## 🌟 Key Features

### Web Interface Features
- **Real-time prediction** with confidence scores
- **Probability breakdown** (Ham vs Spam percentages)
- **Interactive examples** for quick testing
- **Model performance metrics** display
- **Responsive design** for mobile and desktop

### Technical Features
- **Model persistence** using pickle
- **Caching** for improved performance
- **Error handling** and validation
- **Modular code structure**
- **Comprehensive logging**

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **Dataset**: SMS Spam Collection Dataset from UCI ML Repository
- **Libraries**: scikit-learn, NLTK, Streamlit, Gradio, pandas, numpy
- **Inspiration**: Need for effective spam detection in communication systems

## 📞 Contact

- **Author**: [Your Name]
- **Email**: [your.email@example.com]
- **LinkedIn**: [Your LinkedIn Profile]
- **GitHub**: [Your GitHub Profile]

## 🔮 Future Enhancements

- [ ] **Deep Learning models** (LSTM, BERT)
- [ ] **Multi-language support**
- [ ] **Real-time API** deployment
- [ ] **Mobile app** development
- [ ] **Email spam detection** extension
- [ ] **Advanced feature engineering**
- [ ] **Model explainability** (LIME, SHAP)

---

⭐ **Star this repository if you found it helpful!**
