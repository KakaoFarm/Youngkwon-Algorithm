#
# Baekjoon 1932 - 정수 삼각형
# Silver 1
# 다이나믹 프로그래밍
#

import sys

N = int(sys.stdin.readline().rstrip())
triangle = []
dp = []

for _ in range(N):
    row = list(map(int, sys.stdin.readline().rstrip().split()))
    triangle.append(row)
    dp.append([0 for _ in range(len(row))])

dp[0][0] = triangle[0][0]
for i in range(1, N):
    for j in range(0, i+1):
        if j == 0:
            dp[i][j] = dp[i-1][j] + triangle[i][j]
        elif j == i:
            dp[i][j] = dp[i-1][j-1] + triangle[i][j]
        else:
            dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + triangle[i][j]

print(max(dp[N-1]))
