# tests/test_payloads.py

import unittest
from generator.generator import generate_payloads

class TestPayloads(unittest.TestCase):

    def test_generate_payloads(self):
        context = "script"
        payloads = generate_payloads(context)
        self.assertTrue(len(payloads) > 0)

if __name__ == "__main__":
    unittest.main()
