#
# Baekjoon 2293 - 동전 1
# Gold 5
# 다이나믹 프로그래밍
#

import sys
from itertools import combinations_with_replacement


def input(): return sys.stdin.readline().rstrip()


(N, K) = map(int, input().split())
coins = [int(input()) for _ in range(N)]

# dp[K] => K원을 만드는 경우의 수
dp = [0] * (K+1)
dp[0] = 1

for coin in coins:
    for i in range(coin, K+1):
        dp[i] += dp[i-coin]

print(dp[K])
