import unittest

# pyright: reportMissingImports=false
from rearrange import rearrange


class TestRearrange(unittest.TestCase):
    def test_basic(self):
        testcase = "Lovelace, Ada"
        expected = "Ada Lovelace"
        self.assertEqual(rearrange.rerrange_name(testcase), expected)
    
    def test_empty(self):
        testcase = ""
        expected = ""
        self.assertEqual(rearrange.rerrange_name(testcase), expected)

    def test_double_name(self):
        testcase = "Hopper, Grace M."
        expected = "Grace M. Hopper"
        self.assertEqual(rearrange.rerrange_name(testcase), expected)
    
    def test_single_name(self):
        testcase = "Grace"
        expected = "Grace"
        self.assertEqual(rearrange.rerrange_name(testcase), expected)


unittest.main()
