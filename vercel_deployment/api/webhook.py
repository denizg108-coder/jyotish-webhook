#!/usr/bin/env python3
"""
🚀 Jyotish Trading Webhook - Vercel Serverless Function
Optimized for Vercel deployment with zero configuration
"""

from datetime import datetime
import json
import os

def handler(request):
    """Vercel serverless function handler for webhook"""
    
    # Handle CORS for browser requests
    headers = {
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Methods': 'GET, POST, OPTIONS',
        'Access-Control-Allow-Headers': 'Content-Type',
        'Content-Type': 'application/json'
    }
    
    # Handle preflight requests
    if request.method == 'OPTIONS':
        return {
            'statusCode': 200,
            'headers': headers,
            'body': ''
        }
    
    try:
        if request.method == 'GET':
            # GET request - show webhook info
            response_data = {
                'message': '✅ Jyotish Webhook is working perfectly!',
                'status': 'active',
                'service': 'jyotish-trading-webhook',
                'platform': 'vercel-serverless',
                'timestamp': datetime.now().isoformat(),
                'version': '1.0.0',
                'endpoints': {
                    'webhook': '/api/webhook',
                    'health': '/api/health',
                    'home': '/'
                }
            }
            
            return {
                'statusCode': 200,
                'headers': headers,
                'body': json.dumps(response_data, indent=2)
            }
        
        elif request.method == 'POST':
            # POST request - process trading signal
            
            # Parse JSON data
            try:
                if hasattr(request, 'json') and request.json:
                    data = request.json
                elif hasattr(request, 'body'):
                    data = json.loads(request.body) if request.body else {}
                else:
                    data = {}
            except json.JSONDecodeError:
                data = {'raw_data': str(request.body) if hasattr(request, 'body') else 'No data'}
            
            # Extract signal information
            action = data.get('action', 'unknown')
            symbol = data.get('symbol', 'NQ=F')
            price = data.get('price', 'unknown')
            confidence = data.get('confidence', 'unknown')
            
            # Log the signal (Vercel captures console.log)
            print(f"📡 Webhook Signal Received:")
            print(f"   Action: {action}")
            print(f"   Symbol: {symbol}")
            print(f"   Price: {price}")
            print(f"   Confidence: {confidence}")
            print(f"   Timestamp: {datetime.now()}")
            print(f"   Full Data: {json.dumps(data, indent=2)}")
            
            # Create response
            response_data = {
                'status': 'success',
                'message': f'✅ Trading signal received: {action} {symbol}',
                'signal': {
                    'action': action,
                    'symbol': symbol,
                    'price': price,
                    'confidence': confidence,
                    'timestamp': datetime.now().isoformat(),
                    'source': data.get('source', 'unknown')
                },
                'received_data': data,
                'platform': 'vercel-serverless',
                'processing_time': datetime.now().isoformat()
            }
            
            return {
                'statusCode': 200,
                'headers': headers,
                'body': json.dumps(response_data, indent=2)
            }
        
        else:
            # Unsupported method
            return {
                'statusCode': 405,
                'headers': headers,
                'body': json.dumps({
                    'error': f'Method {request.method} not allowed',
                    'allowed_methods': ['GET', 'POST'],
                    'timestamp': datetime.now().isoformat()
                })
            }
            
    except Exception as e:
        # Error handling
        error_response = {
            'status': 'error',
            'message': f'Webhook processing error: {str(e)}',
            'timestamp': datetime.now().isoformat(),
            'platform': 'vercel-serverless'
        }
        
        print(f"❌ Webhook Error: {str(e)}")
        
        return {
            'statusCode': 500,
            'headers': headers,
            'body': json.dumps(error_response, indent=2)
        }

# Vercel entry point
def main(request):
    """Main entry point for Vercel"""
    return handler(request)

# For local testing
if __name__ == "__main__":
    print("🚀 Jyotish Webhook Function Ready for Vercel Deployment")
    print("This function will be available at: /api/webhook")
