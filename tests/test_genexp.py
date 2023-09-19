import unittest

from kata_1.genexp import generate_tshirts_strseq


class TestGenExp(unittest.TestCase):
    def test_generate_thirts_strseq_using_genexp(self):
        colors = ['black', 'white']
        sizes = ['S', 'M', 'L']
        strseq = """black S
black M
black L
white S
white M
white L
"""
        self.assertEquals(generate_tshirts_strseq(colors, sizes), strseq)