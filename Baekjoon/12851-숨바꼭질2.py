#
# Baekjoon 12851 - 숨바꼭질 2
# Gold 4
# 그래프 이론
#

import sys
from collections import deque
input = sys.stdin.readline


N, K = map(int, input().split())
MOVE_RANGE = range(10**5 + 1)
visited = [False for _ in MOVE_RANGE]


def bfs(start):
    q = deque()
    q.append((start, 0))
    visited[start] = 0
    _min = float('inf')
    _cnt = 0

    while q:
        pos, d = q.popleft()

        if pos == K:
            _min = min(_min, d)
            if _min < d:
                return (_min, _cnt)
            visited[pos] = d
            _cnt += 1

        else:
            visited[pos] = d

            if pos-1 in MOVE_RANGE and visited[pos-1] == False:
                q.append((pos-1, d+1))
            if pos+1 in MOVE_RANGE and visited[pos+1] == False:
                q.append((pos+1, d+1))
            if pos*2 in MOVE_RANGE and visited[pos * 2] == False:
                q.append((pos*2, d+1))
    return (_min, _cnt)


_min, _cnt = bfs(N)
print(_min)
print(_cnt)
