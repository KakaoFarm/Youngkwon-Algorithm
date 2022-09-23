#
# Baekjoon 12015 - 가장 긴 증가하는 부분 수열 2
# Gold 2
# 이분 탐색
#

import sys
from bisect import bisect_left
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
LIS = [0]

for elem in A:
    if elem > LIS[-1]:
        LIS.append(elem)
    else:
        LIS[bisect_left(LIS, elem)] = elem

print(len(LIS) - 1)
