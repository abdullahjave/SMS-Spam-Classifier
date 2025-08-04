#!/usr/bin/env python3
"""
Enhanced Gradio App Launcher
Launches the updated spam detection app with comprehensive model results
"""

import subprocess
import sys
import os

def main():
    print("🚀 Launching Enhanced SMS Spam Detection App (Gradio)")
    print("=" * 55)
    print("📊 Features:")
    print("  • 11 ML models tested and compared")
    print("  • Extended Naive Bayes analysis results")
    print("  • Top 3 models performance summary")
    print("  • Clean, mobile-friendly interface")
    print("  • Public sharing capability")
    print("=" * 55)
    
    # Check if gradio is installed
    try:
        import gradio
        print("✅ Gradio is installed")
    except ImportError:
        print("❌ Gradio not found. Installing...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "gradio"])
        print("✅ Gradio installed successfully")
    
    # Check if model files exist
    if not os.path.exists("best_spam_model.pkl"):
        print("⚠️  Model files not found. Please run the Jupyter notebook first to train models.")
        return
    
    print("🌐 Starting Enhanced Gradio App...")
    print("📱 The app will open in your default browser")
    print("🔗 Local URL: http://127.0.0.1:7860")
    print("🌍 Public URL will be shown if sharing is enabled")
    print("\n🛑 Press Ctrl+C to stop the server")
    
    try:
        subprocess.run([sys.executable, "spam_detector_gradio.py"])
    except KeyboardInterrupt:
        print("\n👋 Enhanced Spam Detection App stopped!")

if __name__ == "__main__":
    main()
