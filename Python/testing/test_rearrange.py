import unittest

# pyright: reportMissingImports=false
from rearrange import rearrange


class TestRearrange(unittest.TestCase):
    def test_basic(self):
        testcase = "Lovelace, Ada"
        expected = "Ada Lovelace"
        self.assertEqual(rearrange.rerrange_name(testcase), expected)


unittest.main()
