import sys
from collections import deque
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


def bfs(graph, visit, x, y):
    queue = deque([(x,y)])
    max_x = len(graph[0])
    max_y = len(graph)
    new_entry = []
    breadth = 1
    while True:
        while queue:
            x, y = queue.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if nx < 0 or nx >= max_x or ny < 0 or ny >= max_y:
                    continue
                if graph[ny][nx] != 0:
                    continue
                if visit[ny][nx] == False or visit[ny][nx] > breadth:
                    visit[ny][nx] = breadth
                    new_entry.append((nx, ny))
        if len(new_entry) == 0:
            break
        queue += new_entry
        new_entry = []
        breadth += 1


def solution():
    graph = []
    visit = []
    (m, n) = map(int, sys.stdin.readline().rstrip().split())
    for _ in range(n):
        graph.append(list(map(int, sys.stdin.readline().rstrip().split())))
        visit.append([False] * m)
    
    for y in range(n):
        for x in range(m):
            if graph[y][x] == 1:
                bfs(graph, visit, x, y)
    
    answer = -1            
    for y in range(n):
        for x in range(m):
            if visit[y][x] == False and graph[y][x] == 0:
                return -1
            if answer < visit[y][x]:
                answer = visit[y][x]
            
    return int(answer)
  

print(solution())