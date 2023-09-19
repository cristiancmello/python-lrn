import array
import unittest

from kata_1.array import generate_codes_using_genexp


class TestArray(unittest.TestCase):
    def test_get_codes_from_symbols_more_eff_using_genexp(self):
        symbols = '$¢£¥€¤'
        self.assertEquals(generate_codes_using_genexp(symbols), array.array('I', [36, 162, 163, 165, 8364, 164]))