#
# Baekjoon 2294 - 동전 2
# Gold 5
# 다이나믹 프로그래밍
#

import sys
input = sys.stdin.readline

n, k = map(int, input().split())
coins = []
dp = [float('inf') for _ in range(k + 1)]
for _ in range(n):
    c = int(input())
    if c <= k:
        dp[c] = 1
        coins.append(c)

for i in range(1, k + 1):
    if dp[i] != -1:
        for c in coins:
            if i + c < (k + 1):
                dp[i + c] = min(dp[i + c], dp[i] + 1)

print(dp[k] if dp[k] != float('inf') else -1)
