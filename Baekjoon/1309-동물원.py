# 
# Baekjoon 1309 - 동물원
# Silver 1
# 다이나믹 프로그래밍
# 

import sys

N = int(sys.stdin.readline().rstrip())
# dp[N][0] = 배치 안하는 경우, dp[N][1] = 왼쪽에 배치하는 경우, dp[N][2] = 오른쪽에 배치하는 경우
dp = [[0, 0, 0] for _ in range(N)]  

dp[0][0] = 1
dp[0][1] = 1
dp[0][2] = 1

for i in range(1, N):
    dp[i][0] = (dp[i-1][0] + dp[i-1][1] + dp[i-1][2]) % 9901
    dp[i][1] = (dp[i-1][0] + dp[i-1][2]) % 9901
    dp[i][2] = (dp[i-1][0] + dp[i-1][1]) % 9901

print(sum(dp[N-1]) % 9901)