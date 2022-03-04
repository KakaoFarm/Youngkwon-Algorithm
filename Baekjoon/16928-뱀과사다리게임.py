#
# Baekjoon 16928 - 뱀과 사다리 게임
# Silver 1
# 그래프 이론
#

import sys
from collections import deque
input = sys.stdin.readline


def bfs():
    visited = [0 for _ in range(101)]
    q = deque()
    q.append(1)
    visited[1] = 0
    while q:
        node = q.popleft()
        for i in range(1, 7):
            n = node + i
            if n > 100:
                break
            t = graph[n]
            if visited[t] == 0:
                visited[t] = visited[node] + 1
                q.append(t)
                if t == 100:
                    return visited[100]
    return -1


N, M = map(int, input().split())
graph = [i for i in range(101)]
for _ in range(N + M):
    A, B = map(int, input().split())
    graph[A] = B
print(bfs())
