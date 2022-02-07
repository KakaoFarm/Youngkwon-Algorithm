#
# Baekjoon 2156 - 포도주 시식
# Silver 1
# 다이나믹 프로그래밍
#

import sys

n = int(sys.stdin.readline().rstrip())
grape = [0 for _ in range(max(3, n))]
for i in range(n):
    grape[i] = int(sys.stdin.readline().rstrip())

dp = [0 for _ in range(max(3, n))]
dp[0] = grape[0]
dp[1] = dp[0] + grape[1]
dp[2] = max(grape[0] + grape[2], grape[1] + grape[2], dp[1])

for i in range(3, n):
    dp[i] = max(dp[i-2] + grape[i], dp[i-3] + grape[i-1] + grape[i], dp[i-1])

print(dp[n-1])
