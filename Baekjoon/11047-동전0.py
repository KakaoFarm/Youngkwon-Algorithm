#
# Baekjoon 11074 - 동전 0
# Silver 3
# 그리디 알고리즘
#

import sys
input = sys.stdin.readline

N, K = map(int, input().split())
coins = [int(input()) for _ in range(N)]
coins = sorted(coins, reverse=True)
answer = 0
i = 0

while K > 0 or i < len(coins):
    answer += K // coins[i]
    K = K % coins[i]
    i += 1

print(answer)
