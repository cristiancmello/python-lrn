import math

from time import perf_counter as pc


def call_benchmark() -> int:
    ti = pc()
    list(0 for _ in range(1200000))
    tf = pc() - ti
    return math.trunc(tf * 1000)
