#!/usr/bin/env python3
"""
Main entry point that redirects to Supabase version
"""
from src.main_supabase import app

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
