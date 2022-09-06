#
# Baekjoon 12865 - 평범한 배낭
# Gold 5
# 다이나믹 프로그래밍
#


import sys
input = sys.stdin.readline

N, K = map(int, input().split())
# dp[n][k]에서 n개의 물건까지 순회했을 때, k짜리 배낭에 담을 수 있는 최대 가치
dp = [[0]*(K+1) for _ in range(N+1)]
items = [(0, 0)]
for _ in range(N):
    W, V = map(int, input().split())
    items.append((W, V))

for i in range(1, N+1):
    for j in range(1, K+1):
        W, V = items[i]

        if j < W:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-W] + V)

print(dp[N][K])
