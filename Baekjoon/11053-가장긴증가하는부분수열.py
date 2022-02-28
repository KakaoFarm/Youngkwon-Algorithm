#
# Baekjoon 11053 - 가장 긴 증가하는 부분 수열
# Silver 2
# 다이나믹 프로그래밍
#

import sys
input = sys.stdin.readline

N = int(input())
num = list(map(int, input().split()))
dp = [1 for _ in range(N)]

for i in range(N):
    for j in range(i):
        if num[i] > num[j]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))
