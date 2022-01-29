# 
# Baekjoon 1240 - 노드사이의 거리
# Gold 5 
# 그래프 이론
# 

import sys
from collections import deque

def get_dist(n1, n2):
    queue = deque()
    visited = [False for _ in range(N + 1)]
    queue.append((n1, 0))
    visited[n1] = True
    
    while queue:
        (node, d) = queue.popleft()
        
        if node == n2:
            return d
        
        for i in range(len(graph[node])):
            (next_node, dist) = graph[node][i]
            if visited[next_node] == False:
                visited[next_node] = True
                queue.append((next_node, d + dist))
                

(N, M) = map(int, sys.stdin.readline().rstrip().split())
graph = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    (n1, n2, dist) = map(int, sys.stdin.readline().rstrip().split())
    graph[n1].append((n2, dist))
    graph[n2].append((n1, dist))
    
for _ in range(M):
    (n1, n2) = map(int, sys.stdin.readline().rstrip().split())
    print(get_dist(n1, n2))