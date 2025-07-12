from datetime import datetime
import random
import string

def generate_short_code(length=6):
    """Generates a random short code."""
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def new_url_entry(long_url):
    """Creates a new document for a shortened URL."""
    return {
        "long_url": long_url,
        "short_code": generate_short_code(),
        "created_at": datetime.utcnow(),
        "visits": []  # List of visit timestamps
    }

def log_visit():
    """Returns a timestamp for each visit."""
    return {
        "timestamp": datetime.utcnow()
    }