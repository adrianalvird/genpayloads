# tests/test_integration.py

import unittest
from generator.generator import generate_payloads
from generator.payload_tester import test_payload

class TestIntegration(unittest.TestCase):

    def test_payload_generation_and_testing(self):
        context = "script"
        payloads = generate_payloads(context)
        for payload in payloads:
            result = test_payload(payload)
            # Assuming you're running this test on a controlled environment
            self.assertTrue(result, f"Payload failed: {payload}")

if __name__ == "__main__":
    unittest.main()
