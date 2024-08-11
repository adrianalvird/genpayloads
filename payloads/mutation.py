# payloads/mutation.py

import urllib.parse

def encode_payload(payload):
    """Encodes the payload using URL encoding."""
    return urllib.parse.quote(payload)

def obfuscate_payload(payload):
    """Simple obfuscation by splitting characters."""
    return ''.join([char + ' ' for char in payload]).strip()

# Add more mutation techniques as needed

