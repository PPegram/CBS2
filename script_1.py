# Create updated documentation focused on Gemini Code Assist and simplified deployment

# Update the main Flask app to use mock Gemini for demo purposes (fixed)
simplified_app_py = '''"""
Cultural Bias Shield - Simplified Flask Application
Uses Gemini Code Assist patterns for hackathon demo
"""
from flask import Flask, request, jsonify, render_template_string
from flask_cors import CORS
import json
import logging
from datetime import datetime
import random
import re

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize Flask app
app = Flask(__name__)
CORS(app)

# Mock cultural data (in production, this would be loaded from databases)
HOFSTEDE_DATA = {
    "US": {"PDI": 40, "IDV": 91, "MAS": 62, "UAI": 46, "LTO": 26, "IVR": 68},
    "UK": {"PDI": 35, "IDV": 89, "MAS": 66, "UAI": 35, "LTO": 51, "IVR": 69},
    "JP": {"PDI": 54, "IDV": 46, "MAS": 95, "UAI": 92, "LTO": 88, "IVR": 42},
    "CN": {"PDI": 80, "IDV": 20, "MAS": 66, "UAI": 30, "LTO": 87, "IVR": 24},
    "DE": {"PDI": 35, "IDV": 67, "MAS": 66, "UAI": 65, "LTO": 83, "IVR": 40},
    "FR": {"PDI": 68, "IDV": 71, "MAS": 43, "UAI": 86, "LTO": 63, "IVR": 48},
    "IN": {"PDI": 77, "IDV": 48, "MAS": 56, "UAI": 40, "LTO": 51, "IVR": 26},
    "BR": {"PDI": 69, "IDV": 38, "MAS": 49, "UAI": 76, "LTO": 44, "IVR": 59}
}

# Cultural bias patterns (Generated with Gemini Code Assist)
BIAS_PATTERNS = {
    "western_centric": [
        r"\\b(american dream|melting pot|bootstrap)\\b",
        r"\\b(normal|typical|standard)\\s+(american|western|european)\\b",
        r"\\b(christmas|thanksgiving|easter)\\s+(spirit|season|celebration)\\b"
    ],
    "individualism_bias": [
        r"\\b(self-made|individual success|personal achievement)\\b", 
        r"\\b(be yourself|follow your dreams|personal freedom)\\b",
        r"\\b(independent|self-reliant|personal responsibility)\\b"
    ],
    "economic_assumptions": [
        r"\\b(credit card|mortgage|401k)\\b",
        r"\\b(homeowner|nuclear family|suburb)\\b",
        r"\\b(disposable income|consumer choice)\\b"
    ]
}

class SimplifiedBiasDetector:
    """Simplified bias detector using pattern matching"""
    
    def detect_bias(self, content):
        """Detect cultural bias patterns in content"""
        flags = []
        
        for category, patterns in BIAS_PATTERNS.items():
            for pattern in patterns:
                matches = re.findall(pattern, content, re.IGNORECASE)
                if matches:
                    flags.append({
                        "type": category,
                        "severity": random.randint(4, 8),  # Mock severity
                        "matches": matches,
                        "description": f"Detected {category.replace('_', ' ')} patterns"
                    })
        
        return flags

class SimplifiedCulturalAnalyzer:
    """Simplified cultural analyzer using Hofstede dimensions"""
    
    def analyze_cultural_fit(self, content, countries):
        """Analyze cultural fit for given countries"""
        results = {}
        
        # Keywords for different cultural dimensions
        individualistic_words = ["individual", "personal", "self", "me", "my", "I", "achievement"]
        collectivistic_words = ["community", "team", "we", "our", "together", "family", "group"]
        
        for country in countries:
            if country not in HOFSTEDE_DATA:
                continue
                
            dimensions = HOFSTEDE_DATA[country]
            
            # Simple scoring based on keyword matching
            content_lower = content.lower()
            ind_count = sum(1 for word in individualistic_words if word in content_lower)
            col_count = sum(1 for word in collectivistic_words if word in content_lower)
            
            # Calculate alignment based on country's individualism score
            country_individualism = dimensions["IDV"] / 100.0
            content_individualism = ind_count / max(1, ind_count + col_count)
            
            # Simple alignment calculation
            alignment = 1.0 - abs(country_individualism - content_individualism)
            alignment = max(0.3, min(0.95, alignment))  # Keep realistic range
            
            results[country] = {
                "alignment_score": alignment,
                "cultural_notes": self._generate_cultural_notes(country, dimensions, alignment),
                "recommendations": self._generate_recommendations(country, alignment)
            }
        
        return results
    
    def _generate_cultural_notes(self, country, dimensions, alignment):
        """Generate cultural insights for country"""
        notes = []
        
        if dimensions["IDV"] > 70:
            notes.append(f"{country} values individual achievement and personal freedom")
        else:
            notes.append(f"{country} emphasizes collective harmony and group success")
            
        if alignment < 0.6:
            notes.append("Content may not resonate well with local cultural values")
        
        return notes
    
    def _generate_recommendations(self, country, alignment):
        """Generate recommendations for improving cultural fit"""
        if alignment >= 0.8:
            return ["Content shows good cultural alignment"]
        elif alignment >= 0.6:
            return ["Consider minor cultural adaptations", "Test with local focus groups"]
        else:
            return [
                "Significant cultural adaptation recommended",
                "Consult local cultural experts", 
                "Consider market-specific campaign variants"
            ]

# Initialize components
bias_detector = SimplifiedBiasDetector()
cultural_analyzer = SimplifiedCulturalAnalyzer()

@app.route('/')
def index():
    """Serve simple frontend"""
    html_template = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Cultural Bias Shield</title>
        <style>
            body { font-family: Arial, sans-serif; max-width: 800px; margin: 0 auto; padding: 20px; }
            .header { text-align: center; color: #1976d2; }
            .form-group { margin: 20px 0; }
            label { display: block; margin-bottom: 5px; font-weight: bold; }
            textarea, select { width: 100%; padding: 10px; border: 1px solid #ddd; border-radius: 4px; }
            button { background: #1976d2; color: white; padding: 12px 24px; border: none; border-radius: 4px; cursor: pointer; }
            button:hover { background: #1565c0; }
            .results { margin-top: 20px; padding: 20px; background: #f5f5f5; border-radius: 4px; }
            .country-score { margin: 10px 0; padding: 10px; background: white; border-left: 4px solid #1976d2; }
            .bias-flag { margin: 5px 0; padding: 8px; background: #fff3cd; border-left: 4px solid #ffc107; }
        </style>
    </head>
    <body>
        <div class="header">
            <h1>🛡️ Cultural Bias Shield</h1>
            <p>AI-Powered Campaign Cultural Risk Assessment</p>
        </div>
        
        <form id="analysisForm" onsubmit="analyzeCampaign(event)">
            <div class="form-group">
                <label for="content">Campaign Content:</label>
                <textarea id="content" rows="6" placeholder="Enter your campaign content here..." required></textarea>
            </div>
            
            <div class="form-group">
                <label for="countries">Target Countries (Ctrl+Click for multiple):</label>
                <select id="countries" multiple required>
                    <option value="US">United States</option>
                    <option value="UK">United Kingdom</option>
                    <option value="JP">Japan</option>
                    <option value="CN">China</option>
                    <option value="DE">Germany</option>
                    <option value="FR">France</option>
                    <option value="IN">India</option>
                    <option value="BR">Brazil</option>
                </select>
            </div>
            
            <button type="submit">Analyze Cultural Risk</button>
        </form>
        
        <div id="results" style="display: none;"></div>
        
        <script>
            function analyzeCampaign(event) {
                event.preventDefault();
                
                const content = document.getElementById('content').value;
                const countries = Array.from(document.getElementById('countries').selectedOptions).map(opt => opt.value);
                
                fetch('/api/analyze', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({
                        campaign_content: content,
                        target_countries: countries
                    })
                })
                .then(response => response.json())
                .then(data => displayResults(data))
                .catch(error => console.error('Error:', error));
            }
            
            function displayResults(data) {
                const resultsDiv = document.getElementById('results');
                
                let html = '<div class="results"><h3>Analysis Results</h3>';
                html += `<p><strong>Overall Score:</strong> ${(data.overall_score * 100).toFixed(1)}%</p>`;
                html += `<p><strong>Risk Level:</strong> ${data.risk_level.toUpperCase()}</p>`;
                
                html += '<h4>Country Scores:</h4>';
                for (const [country, score] of Object.entries(data.country_scores)) {
                    html += `<div class="country-score"><strong>${country}:</strong> ${(score * 100).toFixed(1)}%</div>`;
                }
                
                if (data.bias_flags && data.bias_flags.length > 0) {
                    html += '<h4>Potential Issues:</h4>';
                    data.bias_flags.forEach(flag => {
                        html += `<div class="bias-flag"><strong>${flag.type}:</strong> ${flag.description}</div>`;
                    });
                }
                
                html += '</div>';
                resultsDiv.innerHTML = html;
                resultsDiv.style.display = 'block';
            }
        </script>
    </body>
    </html>
    """
    return render_template_string(html_template)

@app.route('/api/analyze', methods=['POST'])
def analyze_campaign():
    """Main analysis endpoint - simplified for hackathon"""
    try:
        data = request.json
        content = data.get('campaign_content', '')
        countries = data.get('target_countries', [])
        
        if not content or not countries:
            return jsonify({"error": "Missing content or countries"}), 400
        
        logger.info(f"Analyzing campaign for countries: {countries}")
        
        # Detect bias patterns
        bias_flags = bias_detector.detect_bias(content)
        
        # Analyze cultural fit
        cultural_results = cultural_analyzer.analyze_cultural_fit(content, countries)
        
        # Calculate scores
        country_scores = {country: result["alignment_score"] 
                         for country, result in cultural_results.items()}
        
        overall_score = sum(country_scores.values()) / len(country_scores) if country_scores else 0
        
        # Determine risk level
        if overall_score >= 0.8:
            risk_level = "low"
        elif overall_score >= 0.6:
            risk_level = "medium"
        else:
            risk_level = "high"
        
        # Generate recommendations
        recommendations = []
        for country, result in cultural_results.items():
            if result["alignment_score"] < 0.7:
                recommendations.extend([
                    f"{country}: {rec}" for rec in result["recommendations"]
                ])
        
        response = {
            "analysis_id": f"analysis_{datetime.now().strftime('%Y%m%d_%H%M%S')}",
            "overall_score": overall_score,
            "country_scores": country_scores,
            "bias_flags": bias_flags,
            "cultural_insights": {
                country: {
                    "cultural_notes": result["cultural_notes"],
                    "alignment_score": result["alignment_score"]
                }
                for country, result in cultural_results.items()
            },
            "recommendations": recommendations,
            "risk_level": risk_level,
            "processing_time": datetime.now().isoformat()
        }
        
        return jsonify(response)
        
    except Exception as e:
        logger.error(f"Analysis error: {str(e)}")
        return jsonify({"error": "Analysis failed", "message": str(e)}), 500

@app.route('/api/countries', methods=['GET'])
def get_countries():
    """Get supported countries"""
    countries = [
        {"code": code, "name": name} for code, name in [
            ("US", "United States"), ("UK", "United Kingdom"), ("JP", "Japan"),
            ("CN", "China"), ("DE", "Germany"), ("FR", "France"),
            ("IN", "India"), ("BR", "Brazil")
        ]
    ]
    return jsonify({"countries": countries, "total_count": len(countries)})

@app.route('/api/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({
        "status": "healthy",
        "timestamp": datetime.now().isoformat(),
        "message": "Cultural Bias Shield is running"
    })

if __name__ == '__main__':
    import os
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
'''

# Save the simplified app
with open('app_hackathon.py', 'w') as f:
    f.write(simplified_app_py)

print("✅ Created app_hackathon.py - Self-contained Flask app with HTML frontend")