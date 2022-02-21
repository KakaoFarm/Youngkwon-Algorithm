#
# Baekjoon 1916 - 최소비용 구하기
# Gold 5
# 그래프 이론, 다익스트라
#

import sys
import heapq
input = sys.stdin.readline


def dijkstra(start):
    dist = [float('inf') for _ in range(N+1)]
    q = []
    heapq.heappush(q, (0, start))
    while q:
        curr_dist, node = heapq.heappop(q)
        if curr_dist < dist[node]:
            dist[node] = curr_dist
            for i in range(1, N+1):
                d = graph[node][i]
                if d > -1:
                    heapq.heappush(q, (curr_dist + d, i))
    return dist


N = int(input())
M = int(input())
graph = [[-1 for _ in range(N+1)] for _ in range(N+1)]
for _ in range(M):
    A, B, W = map(int, input().split())
    graph[A][B] = W if graph[A][B] == -1 else min(graph[A][B], W)
S, E = map(int, input().split())
print(dijkstra(S)[E])
