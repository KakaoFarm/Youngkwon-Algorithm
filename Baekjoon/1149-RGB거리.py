# 
# Baekjoon 1309 - 동물원
# Silver 1
# 다이나믹 프로그래밍
# 

import sys

N = int(sys.stdin.readline().rstrip())

dp = [[0, 0, 0] for _ in range(N)]
cost = []
for _ in range(N):
    cost.append(list(map(int, sys.stdin.readline().rstrip().split())))

dp[0] = cost[0]
for i in range(1, N):
    dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + cost[i][0]
    dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + cost[i][1]
    dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + cost[i][2]

print(min(dp[N-1]))