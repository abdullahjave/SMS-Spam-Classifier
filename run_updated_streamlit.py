#!/usr/bin/env python3
"""
Enhanced Streamlit App Launcher
Launches the updated spam detection app with comprehensive model results
"""

import subprocess
import sys
import os

def main():
    print("🚀 Launching Enhanced SMS Spam Detection App")
    print("=" * 50)
    print("📊 Features:")
    print("  • 11 ML models tested and compared")
    print("  • Extended Naive Bayes analysis")
    print("  • Comprehensive performance metrics")
    print("  • Interactive prediction interface")
    print("  • Updated with latest results")
    print("=" * 50)
    
    # Check if streamlit is installed
    try:
        import streamlit
        print("✅ Streamlit is installed")
    except ImportError:
        print("❌ Streamlit not found. Installing...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "streamlit"])
        print("✅ Streamlit installed successfully")
    
    # Check if model files exist
    if not os.path.exists("best_spam_model.pkl"):
        print("⚠️  Model files not found. Please run the Jupyter notebook first to train models.")
        return
    
    print("🌐 Starting Enhanced Streamlit App...")
    print("📱 The app will open in your default browser")
    print("🔗 URL: http://localhost:8501")
    print("\n🛑 Press Ctrl+C to stop the server")
    
    try:
        subprocess.run([
            sys.executable, "-m", "streamlit", "run", 
            "spam_detector_app.py",
            "--server.headless", "false",
            "--server.port", "8501"
        ])
    except KeyboardInterrupt:
        print("\n👋 Enhanced Spam Detection App stopped!")

if __name__ == "__main__":
    main()
