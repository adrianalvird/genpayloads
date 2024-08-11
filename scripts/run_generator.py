# scripts/run_generator.py

from generator.generator import generate_payloads
from generator.payload_tester import test_payload
from reports.report_generator import generate_report, save_report
from utils.logger import log_message
from utils.http_client import send_request

def main():
    context = "script"  # Example: you might get this from context parsing
    payloads = generate_payloads(context)
    successful_payloads = []

    for payload in payloads:
        if test_payload(payload):
            successful_payloads.append(payload)
            log_message(f"Payload succeeded: {payload}")

    report = generate_report(successful_payloads)
    save_report(report)

if __name__ == "__main__":
    main()

