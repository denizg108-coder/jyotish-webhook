#!/usr/bin/env python3
"""
Home Page - Vercel Serverless Function
"""

from datetime import datetime
import json

def handler(request):
    """Home page with webhook information"""
    
    # For HTML response
    if request.headers.get('Accept', '').find('text/html') >= 0:
        
        html_content = f"""
<!DOCTYPE html>
<html>
<head>
    <title>Jyotish Trading System</title>
    <style>
        body {{ 
            font-family: Arial, sans-serif; 
            max-width: 800px; 
            margin: 50px auto; 
            padding: 20px;
            background: #f5f5f5;
        }}
        .container {{
            background: white;
            padding: 30px;
            border-radius: 10px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        }}
        .status {{ color: #27AE60; font-weight: bold; }}
        .url {{ 
            background: #f8f9fa; 
            padding: 15px; 
            border-radius: 5px; 
            font-family: monospace;
            border-left: 4px solid #007bff;
            margin: 10px 0;
        }}
        .test-link {{ 
            color: #007bff; 
            text-decoration: none;
            padding: 8px 15px;
            background: #e7f3ff;
            border-radius: 5px;
            display: inline-block;
            margin: 5px;
        }}
        .test-link:hover {{ background: #cce7ff; }}
        h1 {{ color: #2c3e50; }}
        h2 {{ color: #34495e; }}
    </style>
</head>
<body>
    <div class="container">
        <h1>🌟 Jyotish Trading System</h1>
        <p><strong>Status:</strong> <span class="status">✅ Operational on Vercel</span></p>
        <p><strong>Platform:</strong> Serverless Functions</p>
        <p><strong>Time:</strong> {datetime.now().strftime("%Y-%m-%d %H:%M:%S UTC")}</p>
        
        <h2>📡 Your Webhook URL:</h2>
        <div class="url">https://your-deployment-url.vercel.app/api/webhook</div>
        
        <h2>🧪 Test Endpoints:</h2>
        <a href="/api/health" class="test-link">Health Check</a>
        <a href="/api/webhook" class="test-link">Webhook Test</a>
        
        <h2>🎯 Usage Instructions:</h2>
        <ol>
            <li><strong>Copy your webhook URL</strong> from above</li>
            <li><strong>Use in TradingView</strong> Pine Script alerts</li>
            <li><strong>Send POST requests</strong> with JSON trading data</li>
            <li><strong>Monitor signals</strong> in Vercel function logs</li>
        </ol>
        
        <h2>📊 Trading Signal Format:</h2>
        <div class="url">
{{
  "action": "buy",
  "symbol": "NQ=F", 
  "price": 12345.67,
  "confidence": 0.92,
  "source": "jyotish_predictor"
}}
        </div>
        
        <hr>
        <p><em>🚀 Ready to receive TradingView signals! Powered by Vercel Serverless Functions.</em></p>
    </div>
</body>
</html>
"""
        
        return {
            'statusCode': 200,
            'headers': {
                'Content-Type': 'text/html',
                'Access-Control-Allow-Origin': '*'
            },
            'body': html_content
        }
    
    # For JSON response
    else:
        headers = {
            'Access-Control-Allow-Origin': '*',
            'Content-Type': 'application/json'
        }
        
        response_data = {
            'service': 'jyotish-trading-webhook',
            'status': 'operational', 
            'platform': 'vercel-serverless',
            'timestamp': datetime.now().isoformat(),
            'endpoints': {
                'webhook': '/api/webhook',
                'health': '/api/health',
                'home': '/'
            },
            'message': 'Jyotish Trading System ready to receive signals'
        }
        
        return {
            'statusCode': 200,
            'headers': headers,
            'body': json.dumps(response_data, indent=2)
        }

# Vercel entry point  
def main(request):
    return handler(request)
