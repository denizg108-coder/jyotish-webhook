#!/usr/bin/env python3
"""
Health Check Endpoint - Vercel Serverless Function
"""

from datetime import datetime
import json

def handler(request):
    """Health check endpoint for monitoring"""
    
    headers = {
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Methods': 'GET',
        'Access-Control-Allow-Headers': 'Content-Type',
        'Content-Type': 'application/json'
    }
    
    health_data = {
        'status': 'healthy',
        'service': 'jyotish-trading-webhook', 
        'platform': 'vercel-serverless',
        'timestamp': datetime.now().isoformat(),
        'version': '1.0.0',
        'uptime': 'serverless',
        'endpoints': {
            'webhook': '/api/webhook',
            'health': '/api/health',
            'home': '/'
        }
    }
    
    return {
        'statusCode': 200,
        'headers': headers,
        'body': json.dumps(health_data, indent=2)
    }

# Vercel entry point
def main(request):
    return handler(request)
