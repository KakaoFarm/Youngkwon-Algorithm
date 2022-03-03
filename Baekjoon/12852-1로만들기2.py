#
# Baekjoon 12852 - 1로 만들기 2
# Silver 1
# 다이나믹 프로그래밍
#

import sys
input = sys.stdin.readline

N = int(input())
dp = [[0, [1]] for _ in range(N+1)]

for x in range(2, N+1):
    candidate = []

    if x % 3 == 0:
        candidate.append(dp[x//3])
    if x % 2 == 0:
        candidate.append(dp[x//2])
    candidate.append(dp[x-1])
    _min = sorted(candidate, key=lambda x: x[0])[0]
    dp[x] = [_min[0] + 1, _min[1] + [x]]

print(dp[N][0])
ans_lst = sorted(dp[N][1], reverse=True)
for i in range(len(ans_lst)):
    if i < len(ans_lst) - 1:
        print(ans_lst[i], end=' ')
    else:
        print(ans_lst[i])
