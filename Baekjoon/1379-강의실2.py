#
# Baekjoon 1379 - 강의실 2
# Gold 3
# 정렬, 그리디 알고리즘
#

import heapq
import sys
input = sys.stdin.readline

N = int(input())

lecture = []
room = [-1 for _ in range(N + 1)]

for _ in range(N):
    lec_num, start, end = map(int, input().split())
    lecture.append((start, end, lec_num))
lecture.sort()

end_q = []
start, end, lec_num = lecture[0]
room[lec_num] = 1
heapq.heappush(end_q, (end, 1))
max_room = 1

for i in range(1, N):
    start, end, lec_num = lecture[i]
    e, r = heapq.heappop(end_q)

    if start >= e:
        room[lec_num] = r
        heapq.heappush(end_q, (end, r))
    else:
        max_room += 1
        room[lec_num] = max_room
        heapq.heappush(end_q, (e, r))
        heapq.heappush(end_q, (end, max_room))

print(max_room)
for i in range(1, N + 1):
    print(room[i])
