# generator/generator.py

from payloads.base_payloads import BASE_PAYLOADS
from payloads.mutation import encode_payload, obfuscate_payload
from payloads.context_aware import generate_context_aware_payload
from payloads.waf_bypass.py import bypass_waf
from config.settings import WAF_SIGNATURES

def generate_payloads(context):
    """Generates a list of mutated and context-aware payloads."""
    payloads = []
    for base_payload in BASE_PAYLOADS:
        context_payload = generate_context_aware_payload(base_payload, context)
        encoded_payload = encode_payload(context_payload)
        obfuscated_payload = obfuscate_payload(encoded_payload)
        waf_bypass_payload = bypass_waf(obfuscated_payload, WAF_SIGNATURES)
        payloads.append(waf_bypass_payload)
    return payloads

