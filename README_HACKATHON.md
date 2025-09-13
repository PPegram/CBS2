# 🛡️ Cultural Bias Shield - Hackathon Quick Start

**Code-focused AI solution using Gemini Code Assist for cultural bias detection**

---

## 🚀 1-Minute Setup

### Prerequisites
- Python 3.8+ installed
- Internet connection for dependencies

### Quick Start
```bash
# 1. Download the files
# 2. Open terminal in project folder
# 3. Run the startup script:

# On Linux/Mac:
chmod +x run.sh
./run.sh

# On Windows:
run.bat

# 4. Open browser to http://localhost:5000
```

**That's it! Your Cultural Bias Shield is running.**

---

## 🎯 What This Does

**Cultural Bias Shield** analyzes marketing campaigns for cultural bias using:

- ✅ **Pattern Recognition** - Detects Western-centric assumptions
- ✅ **Cultural Scoring** - Hofstede dimension analysis for 8 countries  
- ✅ **Bias Detection** - Identifies individualism vs collectivism mismatches
- ✅ **Actionable Insights** - Specific recommendations for each market

### Demo Content Examples

**Test Case 1: Individual Success Focus**
```
"Unlock your potential with our revolutionary fitness app! 
Join millions of successful individuals who have transformed their lives."
```
- **Expected:** High scores for US/UK, lower for Japan/China
- **Reason:** Individualistic language conflicts with collectivist cultures

**Test Case 2: Community Focus**  
```
"Join our wellness community where families support each other 
in achieving health goals together."
```
- **Expected:** Higher scores for Japan/China, good for all markets
- **Reason:** Community-oriented messaging appeals universally

---

## 🧠 How Gemini Code Assist Helps

This solution showcases **Gemini Code Assist** capabilities:

### 1. Intelligent Pattern Recognition
```python
# Gemini Code Assist generated these bias patterns:
BIAS_PATTERNS = {
    "western_centric": [
        r"\b(american dream|melting pot|bootstrap)\b",
        r"\b(normal|typical|standard)\s+(american|western|european)\b"
    ],
    "individualism_bias": [
        r"\b(self-made|individual success|personal achievement)\b",
        r"\b(be yourself|follow your dreams|personal freedom)\b"
    ]
}
```

### 2. Cultural Algorithm Development
```python
# AI-assisted cultural scoring algorithm
def analyze_cultural_fit(self, content, countries):
    # Gemini helped optimize this cultural alignment calculation
    country_individualism = dimensions["IDV"] / 100.0
    content_individualism = ind_count / max(1, ind_count + col_count)
    alignment = 1.0 - abs(country_individualism - content_individualism)
```

### 3. Smart Recommendations Engine
```python
# Code Assist generated contextual recommendations
def _generate_recommendations(self, country, alignment):
    if alignment < 0.7:
        return [
            "Significant cultural adaptation recommended",
            "Consult local cultural experts",
            "Consider market-specific campaign variants"
        ]
```

---

## 📊 Architecture

```
┌─────────────────────────┐
│   Single Flask App      │
│   (app_hackathon.py)    │
├─────────────────────────┤
│ Built-in HTML Frontend  │ ← Simple web interface
│ Pattern-based Detection │ ← Regex + cultural data
│ Hofstede Analysis       │ ← 8-country cultural scoring
│ JSON API Endpoints      │ ← RESTful responses
└─────────────────────────┘
```

### Key Components

**1. Simplified Architecture**
- Single Python file with embedded frontend
- No external APIs required for core functionality
- Built-in cultural datasets
- Pattern-matching bias detection

**2. Cultural Intelligence**
- Hofstede cultural dimensions for 8 major markets
- Individualism vs collectivism scoring
- Cultural keyword analysis
- Country-specific recommendations

**3. Demo-Ready Features**
- Instant results (no API delays)
- Visual scoring interface  
- Clear bias flags and explanations
- Actionable improvement suggestions

---

## 🎬 Demo Script (3 minutes)

### Setup (30 seconds)
"Let me show you Cultural Bias Shield - an AI that prevents cultural marketing disasters."

**[Open localhost:5000]**

### Test 1: Problematic Content (1 minute)
**[Paste individualistic content]**
```
"Unlock your personal potential! Be the individual success story you were meant to be. 
Take personal responsibility for your achievement dreams!"
```

**[Select US, UK, Japan, China]**
**[Click Analyze]**

"Notice the results:
- **US: 89%** - Great alignment with individualistic culture
- **Japan: 43%** - Poor fit with collectivist values  
- **China: 38%** - Major cultural mismatch
- **Risk Level: HIGH**"

### Test 2: Better Content (1 minute)
**[Clear and paste community-focused content]**
```
"Join our wellness community where families and teams support each other 
in achieving health goals together. Our collective success stories inspire everyone."
```

**[Analyze same countries]**

"Much better:
- **All countries: 75-85%** - Good cross-cultural alignment
- **Risk Level: LOW**
- **Bias flags: None detected**"

### Insights (30 seconds)
"The AI detected the individualism bias and provided specific recommendations:
- Replace 'personal success' with 'community wellness'
- Emphasize group benefits over individual achievement
- Test with local cultural experts"

---

## 🔧 Technical Implementation

### File Structure
```
cultural-bias-shield/
├── app_hackathon.py          # Main application (all-in-one)
├── requirements_hackathon.txt # Minimal dependencies  
├── run.sh                     # Linux/Mac startup
├── run.bat                    # Windows startup
└── README_HACKATHON.md       # This file
```

### Dependencies
- **Flask 2.3.3** - Web framework
- **Flask-CORS 4.0.0** - Cross-origin requests
- **Requests 2.31.0** - HTTP library

### Cultural Data
- **Hofstede Dimensions** - Built-in for 8 countries
- **Bias Patterns** - 15+ regex patterns for common biases
- **Cultural Keywords** - Individualistic vs collectivistic language

---

## 🎯 Hackathon Advantages

### 1. Code Focus
✅ **Gemini Code Assist showcase** - AI-generated algorithms  
✅ **Clean implementation** - Single file, well-documented
✅ **Instant setup** - No cloud configuration needed
✅ **Live demo ready** - Works offline

### 2. Innovation  
✅ **Novel application** - Cultural AI bias detection
✅ **Academic grounding** - Hofstede framework implementation  
✅ **Practical value** - Solves real marketing problems
✅ **Scalable concept** - Clear path to production

### 3. Business Impact
✅ **Large market** - Global marketing industry
✅ **Clear problem** - Cultural missteps cost millions
✅ **Immediate value** - Prevents cultural disasters
✅ **Measurable results** - Quantified cultural alignment

---

## 📈 Extending with Real Gemini API

For production deployment, easily upgrade to real Gemini API:

### Step 1: Get Gemini API Key
```bash
# Get key from: https://makersuite.google.com/app/apikey
export GEMINI_API_KEY="your-actual-api-key"
```

### Step 2: Add Gemini Integration
```python
import google.generativeai as genai

# Configure Gemini
genai.configure(api_key=os.environ["GEMINI_API_KEY"])
model = genai.GenerativeModel('gemini-2.5-flash')

# Enhanced cultural analysis
def analyze_with_gemini(self, content, country):
    prompt = f"""
    Analyze this marketing content for cultural appropriateness in {country}:
    
    Content: {content}
    
    Provide cultural fit score (0-1) and specific concerns.
    """
    
    response = model.generate_content(prompt)
    return parse_gemini_response(response.text)
```

### Step 3: Production Features
- Real-time cultural sentiment analysis
- 107+ country support with live API
- Advanced bias detection patterns
- Industry-specific cultural models

---

## 🏆 Success Metrics

### Demo Success Indicators
- ✅ **Works instantly** - No setup failures
- ✅ **Clear results** - Obvious cultural differences shown
- ✅ **Actionable insights** - Specific recommendations provided
- ✅ **Visual impact** - Easy to understand scoring

### Judge Appeal Factors
- **Technical Innovation** - AI + cultural psychology
- **Practical Application** - Solves real business problems
- **Code Quality** - Clean, documented, extensible  
- **Market Potential** - Large addressable opportunity

---

## 🔮 Next Steps

### Phase 1: Enhanced Detection
- Industry-specific bias patterns
- Multi-language content support
- Advanced cultural frameworks (GLOBE, Schwartz)

### Phase 2: AI Integration  
- Full Gemini API integration
- Real-time social sentiment monitoring
- Predictive cultural trend analysis

### Phase 3: Enterprise Features
- A/B testing integration
- Campaign performance correlation
- Multi-team collaboration tools

---

## 📞 Support

### Quick Troubleshooting

**App won't start:**
```bash
# Check Python version
python3 --version  # Should be 3.8+

# Install dependencies manually
pip3 install flask flask-cors requests
python3 app_hackathon.py
```

**Port already in use:**
```bash
# Change port in app_hackathon.py line 350:
app.run(host='0.0.0.0', port=8080, debug=True)  # Changed from 5000
```

**Dependencies fail:**
```bash
# Use virtual environment
python3 -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
pip install -r requirements_hackathon.txt
```

---

**🚀 Ready to showcase cultural AI intelligence! Good luck with your hackathon! 🛡️**