# 
# Baekjoon 11403 - 경로 찾기
# Silver 1
# 그래프 이론, 그래프 탐색
# 

import sys

def dfs(node, is_start):
    if is_start == False:
        visited[node] = True
    adj = graph[node]
    for i in range(len(adj)):
        if adj[i] == 1 and visited[i] == False:
            dfs(i, is_start=False)


N = int(sys.stdin.readline().rstrip())
graph = []

for _ in range(N):
    graph.append(list(map(int, sys.stdin.readline().rstrip().split())))

for i in range(N):
    visited = [False for _ in range(N)]
    dfs(i, is_start=True)
    for v in visited:
        print(int(v), end=' ')
    print()