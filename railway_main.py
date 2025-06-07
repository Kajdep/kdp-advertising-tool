#!/usr/bin/env python3
"""
Main entry point for KDP Advertising Tool - Railway Compatible
This file properly handles Railway's PORT environment variable
"""
import os
import sys

# Add the current directory to Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

def create_app():
    """Create and configure the Flask application"""
    try:
        # Import the Supabase-powered app
        from src.main_supabase import app
        return app
    except ImportError as e:
        print(f"Error importing Supabase app: {e}")
        # Fallback to a basic Flask app
        from flask import Flask, jsonify
        app = Flask(__name__)
        
        @app.route('/')
        def home():
            return jsonify({
                "status": "error",
                "message": "Supabase app failed to load",
                "error": str(e)
            })
        
        @app.route('/health')
        def health():
            return jsonify({
                "status": "unhealthy",
                "service": "KDP Advertising Tool",
                "error": str(e)
            })
        
        return app

# Create the app instance
app = create_app()

if __name__ == '__main__':
    # Get port from Railway environment variable
    port = int(os.environ.get('PORT', 5000))
    
    print(f"Starting KDP Advertising Tool on port {port}")
    print(f"Environment PORT variable: {os.environ.get('PORT', 'Not set')}")
    
    # Run the app with proper Railway configuration
    app.run(
        host='0.0.0.0',  # Listen on all interfaces
        port=port,       # Use Railway's assigned port
        debug=False      # Production mode
    )

