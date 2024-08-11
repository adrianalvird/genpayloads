# generator/payload_tester.py

import requests
from config.settings import TARGET_URL, REQUEST_HEADERS

def test_payload(payload):
    """Tests the given payload against the target URL."""
    response = requests.get(TARGET_URL, params={'input': payload}, headers=REQUEST_HEADERS)
    return payload in response.text

