#
# Baekjoon 13594 - 숨바꼭질 3
# Gold 5
# 그래프 이론
#

import sys
from collections import deque
input = sys.stdin.readline
MOVE_RANGE = range(0, 10**5 + 1)


def bfs(start_node):
    q = deque()
    q.append(start_node)
    visited = [-1] * (10**5 + 1)
    visited[start_node] = 0

    while q:
        pos = q.popleft()
        if pos == K:
            return visited[pos]

        # 뒤로 이동
        if pos-1 in MOVE_RANGE and visited[pos-1] == -1:
            visited[pos-1] = visited[pos] + 1
            q.append(pos-1)

        # 순간이동
        if pos*2 in MOVE_RANGE and visited[pos*2] == -1:
            visited[pos*2] = visited[pos]
            q.appendleft(pos*2)

        # 앞으로 이동
        if pos+1 in MOVE_RANGE and visited[pos+1] == -1:
            visited[pos+1] = visited[pos] + 1
            q.append(pos+1)


N, K = map(int, input().split())
print(bfs(N))
