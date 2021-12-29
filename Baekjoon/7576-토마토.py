import sys
from collections import deque
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


def bfs(graph):
    queue = deque([])
    for y in range(len(graph)):
        for x in range(len(graph[0])):
            if graph[y][x] == 1:
                queue.append((x, y))
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= len(graph[0]) or ny < 0 or ny >= len(graph):
                continue
            if graph[ny][nx] == 0:
                graph[ny][nx] = graph[y][x] + 1
                queue.append((nx, ny))


def solution():
    graph = []
    (m, n) = map(int, sys.stdin.readline().rstrip().split())
    for _ in range(n):
        graph.append(list(map(int, sys.stdin.readline().rstrip().split())))        
    bfs(graph)
    answer = -1
    for row in graph:
        if 0 in row:
            return -1
        answer = max(answer, max(row))      
    return int(answer) - 1
  

print(solution())