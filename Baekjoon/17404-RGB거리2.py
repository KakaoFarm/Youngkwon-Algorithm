#
# Baekjoon 17404 - RGB거리 2
# Gold 4
# 다이나믹 프로그래밍
#

import sys
input = sys.stdin.readline


N = int(input())
dp = [[0, 0, 0] for _ in range(N+1)]
cost = [[0, 0, 0]]
for _ in range(N):
    cost.append(list(map(int, input().split())))

dp[1] = cost[1]
answer = []
for k in range(3):
    init = k
    dp[2][init] = float('inf')
    dp[2][(init + 1) % 3] = dp[1][init] + cost[2][(init + 1) % 3]
    dp[2][(init + 2) % 3] = dp[1][init] + cost[2][(init + 2) % 3]

    for i in range(3, N + 1):
        dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + cost[i][0]
        dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + cost[i][1]
        dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + cost[i][2]

    answer.append(min(dp[N][(init + 1) % 3], dp[N][(init + 2) % 3]))
print(min(answer))
