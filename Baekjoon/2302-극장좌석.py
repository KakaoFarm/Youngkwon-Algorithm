#
# Baekjoon 2302 - 극장좌석
# Silver 1
# 다이나믹 프로그래밍
#

import sys


def input(): return sys.stdin.readline().rstrip()


N = int(input())
num_of_fix = int(input())
seat_size = []

before = -1
for _ in range(num_of_fix):
    fix_seat = int(input()) - 1
    seat_size.append(fix_seat - before - 1)
    before = fix_seat
seat_size.append(N - before - 1)

max_space = max(seat_size)
dp = [1] * (max_space + 1)

for i in range(2, max_space+1):
    dp[i] = dp[i-1] + dp[i-2]

answer = 1
for size in seat_size:
    answer *= dp[size]
print(answer)
