@echo off
REM Cultural Bias Shield - Windows Run Script

echo 🛡️ Starting Cultural Bias Shield...

REM Check if Python is available
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Python not found. Please install Python 3.8+ first.
    pause
    exit /b 1
)

REM Install dependencies
echo 📦 Installing dependencies...
pip install -r requirements_hackathon.txt

REM Set environment variables
set FLASK_APP=app_hackathon.py
set FLASK_ENV=development

REM Run the application
echo 🚀 Starting server at http://localhost:5000
echo Press Ctrl+C to stop
python app_hackathon.py

pause
