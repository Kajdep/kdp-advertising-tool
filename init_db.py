#!/usr/bin/env python3
"""
Database initialization script for KDP Advertising Tool
"""

import os
import sys

# Add the src directory to the Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from src.main import app
from src.models.user import db

def init_database():
    """Initialize the database with all tables"""
    with app.app_context():
        # Create all tables
        db.create_all()
        print("Database tables created successfully!")
        
        # Create a default user for demo purposes
        from src.models.user import User
        
        # Check if demo user already exists
        demo_user = User.query.filter_by(email='demo@kdptool.com').first()
        if not demo_user:
            demo_user = User(
                name='Demo User',
                email='demo@kdptool.com'
            )
            db.session.add(demo_user)
            db.session.commit()
            print("Demo user created successfully!")
        else:
            print("Demo user already exists.")

if __name__ == '__main__':
    init_database()

