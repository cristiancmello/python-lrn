import unittest

from kata_1.tuple import *


class TestTuple(unittest.TestCase):
    def test_get_codes_from_symbols_more_eff_using_genexp(self):
        symbols = '$¢£¥€¤'
        self.assertTupleEqual(generate_codes_using_genexp(symbols), (36, 162, 163, 165, 8364, 164))
