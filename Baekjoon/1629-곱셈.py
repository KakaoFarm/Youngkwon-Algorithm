#
# Baekjoon 1629 - 곱셈
# Silver 1
# 수학, pow
#

import sys
input = sys.stdin.readline

A, B, C = map(int, input().split())
print(pow(A, B, C))
