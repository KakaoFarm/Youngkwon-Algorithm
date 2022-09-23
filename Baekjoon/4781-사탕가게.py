#
# Baekjoon 4781 - 사탕 가게
# Gold 4
# 다이나믹 프로그래밍
#

import sys
input = sys.stdin.readline


def dp():
    mem = [0 for _ in range(m + 1)]
    for i in range(m + 1):
        for v, c in candy:
            if i + c in range(m + 1):
                mem[i + c] = max(mem[i + c], mem[i] + v)
    return mem[m]


while True:
    n, m = map(float, input().split())
    n = int(n)
    m = int(m * 100 + 0.5)
    if n == 0:
        break

    candy = []
    for _ in range(n):
        v, c = map(float, input().split())
        candy.append((int(v), int(c * 100 + 0.5)))
    print(dp())
