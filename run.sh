#!/bin/bash
# Cultural Bias Shield - Easy Run Script for Hackathon

echo "🛡️ Starting Cultural Bias Shield..."

# Check if Python is available
if ! command -v python3 &> /dev/null; then
    echo "❌ Python3 not found. Please install Python 3.8+ first."
    exit 1
fi

# Check if pip is available
if ! command -v pip3 &> /dev/null; then
    echo "❌ pip3 not found. Please install pip first."
    exit 1
fi

# Install dependencies
echo "📦 Installing dependencies..."
pip3 install -r requirements_hackathon.txt

# Set environment variables
export FLASK_APP=app_hackathon.py
export FLASK_ENV=development

# Run the application
echo "🚀 Starting server at http://localhost:5000"
echo "Press Ctrl+C to stop"
python3 app_hackathon.py
