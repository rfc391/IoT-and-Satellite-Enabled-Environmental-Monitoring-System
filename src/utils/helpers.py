
"""Utilities Module - Shared Helper Functions"""

from datetime import datetime

def generate_timestamp():
    """Generate a current timestamp"""
    return datetime.now().isoformat()
