#
# Baekjoon 2407 - 조합
# Silver 3
# 수학
#

import sys
import operator as op
from functools import reduce
input = sys.stdin.readline


def nCr(n, r):
    if n < 1 or r < 0 or n < r:
        raise ValueError
    r = min(r, n-r)
    numerator = reduce(op.mul, range(n, n-r, -1), 1)
    denominator = reduce(op.mul, range(1, r+1), 1)
    return numerator // denominator


N, M = map(int, input().split())
print(nCr(N, M))
