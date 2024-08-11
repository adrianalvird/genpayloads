# config/settings.py

WAF_SIGNATURES = [
    # Add known WAF signatures that you want to bypass
    'alert',
    '<script>',
    'onerror',
    # Add more as needed
]

# General settings
TARGET_URL = "http://example.com"
REQUEST_HEADERS = {
    'User-Agent': 'XSS-Payload-Generator/1.0',
    # Add any other headers you need
}

