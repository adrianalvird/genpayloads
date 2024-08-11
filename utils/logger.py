# utils/logger.py

import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("XSS-Payload-Generator")

def log_message(message):
    """Logs a message to the console."""
    logger.info(message)
