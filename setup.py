#!/usr/bin/env python3
"""
Setup script for SMS Spam Detection System
Installs all required dependencies and downloads NLTK data
"""

import subprocess
import sys
import os

def install_requirements():
    """Install Python packages from requirements.txt"""
    try:
        print("Installing Python packages...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("✅ Python packages installed successfully!")
    except subprocess.CalledProcessError as e:
        print(f"❌ Error installing packages: {e}")
        return False
    return True

def download_nltk_data():
    """Download required NLTK data"""
    try:
        print("Downloading NLTK data...")
        import nltk
        nltk.download('punkt', quiet=True)
        nltk.download('stopwords', quiet=True)
        nltk.download('punkt_tab', quiet=True)
        print("✅ NLTK data downloaded successfully!")
    except Exception as e:
        print(f"❌ Error downloading NLTK data: {e}")
        return False
    return True

def verify_installation():
    """Verify that all components are working"""
    try:
        print("Verifying installation...")
        
        # Test imports
        import streamlit
        import gradio
        import pandas
        import numpy
        import sklearn
        import nltk
        import matplotlib
        import seaborn
        import pickle
        
        # Test model files
        if os.path.exists('best_spam_model.pkl') and os.path.exists('tfidf_vectorizer.pkl'):
            print("✅ Model files found!")
        else:
            print("⚠️  Model files not found. Please run the Jupyter notebook first.")
        
        print("✅ Installation verified successfully!")
        return True
        
    except ImportError as e:
        print(f"❌ Import error: {e}")
        return False

def main():
    """Main setup function"""
    print("🚀 SMS Spam Detection System Setup")
    print("=" * 50)
    
    # Install requirements
    if not install_requirements():
        print("❌ Setup failed at package installation")
        return
    
    # Download NLTK data
    if not download_nltk_data():
        print("❌ Setup failed at NLTK data download")
        return
    
    # Verify installation
    if not verify_installation():
        print("❌ Setup failed at verification")
        return
    
    print("\n🎉 Setup completed successfully!")
    print("\nNext steps:")
    print("1. Run Jupyter notebook: jupyter notebook spam_system.ipynb")
    print("2. Train the model (if not already done)")
    print("3. Launch web app:")
    print("   - Streamlit: streamlit run spam_detector_app.py")
    print("   - Gradio: python spam_detector_gradio.py")

if __name__ == "__main__":
    main()
