#
# Baekjoon 2579 - 계단 오르기
# Silver 3
# 다이나믹 프로그래밍
#

import sys
input = sys.stdin.readline

N = int(input())
dp = [[0, 0] for _ in range(N+1)]  # 직전 계단을 안밟고 밟음, 직전 계단을 밟고 밟음
s = [0]
for _ in range(N):
    s.append(int(input()))

dp[1] = [s[1], s[1]]
if N > 1:
    dp[2] = [s[2], s[1] + s[2]]
    for i in range(3, N+1):
        dp[i] = [max(dp[i-2][0], dp[i-2][1]) + s[i], dp[i-1][0] + s[i]]
print(max(dp[N]))
