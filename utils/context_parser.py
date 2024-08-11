# utils/context_parser.py

from bs4 import BeautifulSoup

def parse_html_for_context(html):
    """Parses HTML and returns possible injection points."""
    soup = BeautifulSoup(html, 'html.parser')
    contexts = []

    # Example: Find all script tags
    for script in soup.find_all('script'):
        contexts.append(('script', script))

    # Add more parsing logic as needed
    return contexts

