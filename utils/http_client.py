# utils/http_client.py

import requests

def send_request(url, params=None, headers=None):
    """Sends an HTTP GET request and returns the response."""
    response = requests.get(url, params=params, headers=headers)
    return response

