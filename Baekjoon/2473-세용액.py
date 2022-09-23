#
# Baekjoon 2473 - 세 용액
# Gold 3
# 투 포인터
#

import sys
from itertools import combinations
input = sys.stdin.readline

N = int(input())
lst = list(map(int, input().split()))
lst.sort()


nearest = float('inf')
answer = [-1, -1, -1]
start = 0
end = N - 1

for i in range(N-2):
    start = i + 1
    end = N - 1

    while True:
        if end <= start:
            break
        value = lst[i] + lst[start] + lst[end]
        if abs(value) < nearest:
            nearest = abs(value)
            answer = [lst[i], lst[start], lst[end]]
        if value > 0:
            end -= 1
        elif value < 0:
            start += 1
        else:
            break
    if nearest == 0:
        break


print(answer[0], answer[1], answer[2])
