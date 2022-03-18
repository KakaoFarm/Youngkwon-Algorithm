#
# Baekjoon 2211 - 네트워크 복구
# Gold 2
# 그래프 이론, 다익스트라
#

import sys
import heapq
input = sys.stdin.readline


def dijkstra(start_node):
    answer = {i: '' for i in range(2, N + 1)}
    dist = [float('inf')] * (N + 1)
    dist[start_node] = 0
    q = [start_node]
    while q:
        node = heapq.heappop(q)
        for adj, weight in graph[node].items():
            if dist[adj] > dist[node] + weight:
                dist[adj] = dist[node] + weight
                heapq.heappush(q, adj)
                answer[adj] = node
    return answer


N, M = map(int, input().split())
graph = {}
for _ in range(M):
    a, b, w = map(int, input().split())
    if a not in graph:
        graph[a] = {}
    if b not in graph:
        graph[b] = {}

    if b not in graph[a]:
        graph[a][b] = w
    else:
        graph[a][b] = min(graph[a][b], w)
    if a not in graph[b]:
        graph[b][a] = w
    else:
        graph[b][a] = min(graph[b][a], w)


answer = dijkstra(1)
print(len(answer))
for end, start in answer.items():
    print(end, start)
