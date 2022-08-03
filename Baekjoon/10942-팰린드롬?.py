#
# Baekjoon 1197 - 팰린드롬?
# Gold 4
# 다이나믹 프로그래밍
#

import sys
input = sys.stdin.readline

N = int(input())
dp = [[0 for i in range(N)] for j in range(N)]
s = list(map(int, input().split()))
M = int(input())

for b in range(N):
    for start in range(N):
        end = start + b
        if end >= N:
            break
        if start == end:
            dp[start][end] = 1
            continue
        if start + 1 == end and s[start] == s[end]:
            dp[start][end] = 1
            continue
        if s[start] == s[end] and dp[start + 1][end - 1] == 1:
            dp[start][end] = 1

for _ in range(M):
    a, b = map(int, input().split())
    print(dp[a - 1][b - 1])
