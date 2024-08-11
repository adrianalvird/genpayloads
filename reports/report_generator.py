# reports/report_generator.py

def generate_report(successful_payloads):
    """Generates an HTML report of successful payloads."""
    report_html = "<html><head><title>XSS Payload Report</title></head><body>"
    report_html += "<h1>Successful XSS Payloads</h1><ul>"
    
    for payload in successful_payloads:
        report_html += f"<li>{payload}</li>"
    
    report_html += "</ul></body></html>"
    return report_html

def save_report(html_content, filename="report.html"):
    """Saves the generated report to an HTML file."""
    with open(filename, 'w') as f:
        f.write(html_content)
