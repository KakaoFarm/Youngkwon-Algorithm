#
# Baekjoon 11725 - 트리의 부모 찾기
# Silver 2
# 그래프 이론, 트리
#

import sys
from collections import deque
input = sys.stdin.readline


def bfs():
    parents = [-1 for _ in range(N+1)]
    q = deque()
    q.append((1, 1))  # dist, parent, current
    parents[1] = 0
    while q:
        d, c = q.popleft()
        for adj in graph[c]:
            if parents[adj] == -1:
                parents[adj] = c
                q.append((d + 1, adj))
    return parents[2:]


N = int(input())
graph = {}
for _ in range(N-1):
    A, B = map(int, input().split())
    if A not in graph:
        graph[A] = []
    if B not in graph:
        graph[B] = []
    graph[A].append(B)
    graph[B].append(A)

answer = bfs()
for a in answer:
    print(a)
