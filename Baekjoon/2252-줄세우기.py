#
# Baekjoon 2252 - 줄 세우기
# Gold 3
# 우선순위 큐, 위상정렬
#

import heapq
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
degree = [0 for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    degree[b] += 1

queue = []
for i in range(1, N + 1):
    if degree[i] == 0:
        heapq.heappush(queue, i)

answer = []
while queue:
    elem = heapq.heappop(queue)
    answer.append(elem)
    for longer in graph[elem]:
        degree[longer] -= 1
        if degree[longer] == 0:
            heapq.heappush(queue, longer)

print(str(answer)[1: -1].replace(', ', ' '))
