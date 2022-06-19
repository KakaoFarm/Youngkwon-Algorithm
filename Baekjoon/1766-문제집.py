#
# Baekjoon 1766 - 문제집
# Gold 2
# 우선순위 큐, 위상정렬
#

import sys
import heapq
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
visited = [False for _ in range(N+1)]
no_pre = [0 for _ in range(N+1)]
answer = []
q = []
for _ in range(M):
    a, b = map(int, input().split())
    heapq.heappush(graph[a], b)
    no_pre[b] += 1


for i in range(1, N+1):
    if no_pre[i] == 0:
        heapq.heappush(q, i)

while q:
    value = heapq.heappop(q)
    answer.append(value)
    for p in graph[value]:
        no_pre[p] -= 1
        if no_pre[p] == 0:
            heapq.heappush(q, p)


print(' '.join(map(str, answer)))
