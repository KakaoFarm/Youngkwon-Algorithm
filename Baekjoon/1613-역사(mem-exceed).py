#
# Baekjoon 1613 - 역사
# Gold 3
# 그래프 이론
# BFS로 풀이 시도, 메모리 초과
#

import sys
from collections import deque
def input(): return sys.stdin.readline().rstrip()


def bfs(a, b):
    if a in graph[b]:
        return 1

    q = deque()
    q.append(a)

    while q:
        node = q.popleft()
        if b in graph[node]:
            return -1
        else:
            for after in graph[node]:
                q.append(after)
    return 0


(N, K) = map(int, input().split())
# graph[a]에 b가 포함되어 있으면 a < b
graph = [[] for _ in range(N+1)]

for _ in range(K):
    (a, b) = map(int, input().split())
    graph[a].append(b)


T = int(input())
for _ in range(T):
    (ta, tb) = map(int, input().split())
    print(bfs(ta, tb))
