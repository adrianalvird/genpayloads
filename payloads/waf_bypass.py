# payloads/waf_bypass.py

import re

def bypass_waf(payload, waf_signatures):
    """Modifies the payload to bypass known WAF signatures."""
    for signature in waf_signatures:
        payload = re.sub(signature, lambda x: obfuscate_signature(x.group()), payload)
    return payload

def obfuscate_signature(signature):
    """Obfuscates a given WAF signature."""
    return ''.join(['&#' + str(ord(char)) + ';' for char in signature])
