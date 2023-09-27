import unittest

from kata_1.perfcounter import call_benchmark


class TestPerfCounter(unittest.TestCase):
    def test_calling_benchmark_using_perfcounter(self):
        self.assertGreater(call_benchmark(), 0)
