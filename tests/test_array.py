import unittest

from kata_1.array import *


class TestArray(unittest.TestCase):
    def test_get_codes_from_symbols_more_eff_using_genexp(self):
        symbols = '$¢£¥€¤'
        self.assertEqual(generate_codes_using_genexp(symbols), array('I', [36, 162, 163, 165, 8364, 164]))
