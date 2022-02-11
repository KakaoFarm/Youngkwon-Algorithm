#
# Baekjoon 1238 - 파티
# Gold 3
# 그래프 이론, 다익스트라
#

import sys
from queue import PriorityQueue
def input(): return sys.stdin.readline().rstrip()


# 가는 거리를 계산하는 Dijkstra
def going_dijkstra(end_node):
    dist = [float('inf') for _ in range(N + 1)]
    q = PriorityQueue()
    q.put((0, end_node))
    while q.qsize() > 0:
        (curr_dist, node) = q.get()
        if curr_dist < dist[node]:
            dist[node] = curr_dist
            for key, distance in rev_graph[node].items():
                new_dist = curr_dist + distance
                q.put((new_dist, key))
    return dist


# 돌아오는 거리를 계산하는 Dijkstra
def coming_dijkstra(start_node):
    dist = [float('inf') for _ in range(N + 1)]
    q = PriorityQueue()
    q.put((0, start_node))
    while q.qsize() > 0:
        (curr_dist, node) = q.get()
        if curr_dist < dist[node]:
            dist[node] = curr_dist
            for key, distance in graph[node].items():
                new_dist = curr_dist + distance
                q.put((new_dist, key))
    return dist


(N, M, X) = map(int, input().split())
graph = [{} for _ in range(N+1)]
rev_graph = [{} for _ in range(N+1)]

for _ in range(M):
    (start, end, dist) = map(int, input().split())
    graph[start][end] = dist
    rev_graph[end][start] = dist

going_dist = going_dijkstra(end_node=X)
coming_dist = coming_dijkstra(start_node=X)
answer = [0] * N
for i in range(1, N + 1):
    answer[i-1] = going_dist[i] + coming_dist[i]
print(max(answer))
