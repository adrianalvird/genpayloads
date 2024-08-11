# tests/test_mutation.py

import unittest
from payloads.mutation import encode_payload, obfuscate_payload

class TestMutation(unittest.TestCase):

    def test_encode_payload(self):
        payload = "<script>alert(1)</script>"
        encoded = encode_payload(payload)
        self.assertIn("%3Cscript%3Ealert%281%29%3C%2Fscript%3E", encoded)

    def test_obfuscate_payload(self):
        payload = "alert(1)"
        obfuscated = obfuscate_payload(payload)
        self.assertEqual(obfuscated, "a l e r t ( 1 )")

if __name__ == "__main__":
    unittest.main()

