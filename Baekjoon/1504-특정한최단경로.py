#
# Baekjoon 1504 - 특정한 최단 경로
# Gold 4
# 그래프 이론, 다익스트라
#

import sys
import heapq
input = sys.stdin.readline


def dijkstra(start_node):
    dist = [float('inf') for _ in range(N+1)]
    q = []
    heapq.heappush(q, (0, start_node))
    while q:
        curr_dist, node = heapq.heappop(q)
        if curr_dist < dist[node]:
            dist[node] = curr_dist
            for i in range(1, N+1):
                d = graph[node][i]
                if d != -1:
                    heapq.heappush(q, (curr_dist + d, i))
    return dist


N, E = map(int, input().split())
graph = [[-1 for _ in range(N+1)] for _ in range(N+1)]
for _ in range(E):
    N1, N2, W = map(int, input().split())
    graph[N1][N2] = W
    graph[N2][N1] = W
R1, R2 = map(int, input().split())

start_dist = dijkstra(1)
R1_dist = dijkstra(R1)
R2_dist = dijkstra(R2)
answer = min(start_dist[R1] + R1_dist[R2] + R2_dist[N],
             start_dist[R2] + R2_dist[R1] + R1_dist[N])
print(answer if answer < float('inf') else -1)
