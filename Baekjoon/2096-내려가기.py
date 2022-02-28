#
# Baekjoon 2096 - 내려가기
# Gold 4
# 다이나믹 프로그래밍, 슬라이딩 윈도우
#

import sys
input = sys.stdin.readline

N = int(input())
max_dp = [0, 0, 0]
min_dp = [0, 0, 0]
for _ in range(N):
    a, b, c = map(int, input().split())

    # max
    max_dp = [max(max_dp[0], max_dp[1]) + a, max(max_dp[0],
                                                 max_dp[1], max_dp[2]) + b, max(max_dp[1], max_dp[2]) + c]
    # min
    min_dp = [min(min_dp[0], min_dp[1]) + a, min(min_dp[0],
                                                 min_dp[1], min_dp[2]) + b, min(min_dp[1], min_dp[2]) + c]

_max = max(max_dp)
_min = min(min_dp)
print(_max, _min)
