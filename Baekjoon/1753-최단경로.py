# 
# Baekjoon 1753 - 최단경로
# Gold 5
# 그래프 이론, 다익스트라
# 

import sys
from queue import PriorityQueue

def dijkstra(start_node):
    dist = [float('inf') for _ in range(V + 1)]
    
    q = PriorityQueue()
    q.put((0, start_node))

    while q.qsize() > 0:
        (curr_dist, node) = q.get()
        if curr_dist <= dist[node]:
            dist[node] = curr_dist
            for key, distance in graph[node].items():
                new_dist = curr_dist + distance
                if new_dist < dist[key]:
                    dist[key] = new_dist
                    q.put((new_dist, key))
                
    return dist[1:]     


(V, E) = map(int, sys.stdin.readline().rstrip().split())
start_node = int(sys.stdin.readline().rstrip())
graph = [{} for _ in range(V+1)]

for _ in range(E):
    (u, v, w) = map(int, sys.stdin.readline().rstrip().split())
    if v in graph[u].keys():
        graph[u][v] = min(graph[u][v], w)
    else:
        graph[u][v] = w

answer = dijkstra(start_node)
for ans in answer:
    if ans == float('inf'):
        print("INF")
    else:
        print(ans)