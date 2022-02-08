#
# Baekjoon 2225 - 합분해
# Gold 5
# 다이나믹 프로그래밍
#

import sys

(N, K) = map(int, sys.stdin.readline().rstrip().split())
dp = [[0] * (K+1) for _ in range(N+1)]

for i in range(N+1):
    dp[i][1] = 1
    dp[i][2] = i + 1

for j in range(K+1):
    dp[1][j] = j

for i in range(2, N+1):
    for j in range(1, K+1):
        dp[i][j] = (dp[i-1][j] + dp[i][j-1]) % 1000000000

print(dp[N][K] % 1000000000)
