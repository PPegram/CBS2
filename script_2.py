# Create simplified requirements for hackathon
hackathon_requirements = '''# Cultural Bias Shield - Hackathon Requirements
# Simplified dependencies for code-focused hackathon

Flask==2.3.3
flask-cors==4.0.0
requests==2.31.0
'''

with open('requirements_hackathon.txt', 'w') as f:
    f.write(hackathon_requirements)

print("✅ Created requirements_hackathon.txt - Minimal dependencies")

# Create a run script for easy startup
run_script = '''#!/bin/bash
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
'''

with open('run.sh', 'w') as f:
    f.write(run_script)

print("✅ Created run.sh - One-command startup script")

# Create Windows batch file
run_bat = '''@echo off
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
'''

with open('run.bat', 'w') as f:
    f.write(run_bat)

print("✅ Created run.bat - Windows startup script")