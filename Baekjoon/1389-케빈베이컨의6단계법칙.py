#
# Baekjoon 1389 - 케빈 베이컨의 6단계 법칙
# Silver 1
# 그래프 이론
#

import sys
from collections import deque
input = sys.stdin.readline


def bfs(person):
    visit = [float('inf')] * (N+1)
    q = deque()
    q.append((0, person))
    visit[person] = 0
    while q:
        (dist, p) = q.popleft()
        for friend in graph[p]:
            if visit[friend] == float('inf'):
                visit[friend] = dist + 1
                q.append((dist+1, friend))
    return sum(visit[1:])


N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    A, B = map(int, input().split())
    if B not in graph[A]:
        graph[A].append(B)
        graph[B].append(A)

kb = []
for i in range(1, N):
    kb.append(bfs(i))
print(kb.index(min(kb)) + 1)
