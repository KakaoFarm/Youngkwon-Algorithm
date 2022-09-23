#
# Baekjoon 2467 - 용액
# Gold 5
# 투 포인터
#

import sys
input = sys.stdin.readline

N = int(input())
lst = list(map(int, input().split()))
lst.sort()

start = 0
end = N - 1

nearest = float('inf')
answer = [-1, -1]
while True:
    if end <= start:
        break
    value = lst[start] + lst[end]
    if abs(value) < nearest:
        nearest = abs(value)
        answer = [lst[start], lst[end]]
    if value > 0:
        end -= 1
    elif value < 0:
        start += 1
    else:
        break
print(answer[0], answer[1])
