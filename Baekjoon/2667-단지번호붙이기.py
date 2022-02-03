# 
# Baekjoon 2667 - 단지번호붙이기
# Silver 1
# 그래프 이론
# 

import sys

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
nov = 0

def dfs(i, j):
    if visited[i][j] == True:
        return False
    visited[i][j] = True
    global nov
    nov += 1
    for k in range(4):
        new_x = i + dx[k]
        new_y = j + dy[k]
        if new_x in index_range and new_y in index_range and graph[new_x][new_y] == 1:
            dfs(new_x, new_y)
    
    return True
    

N = int(sys.stdin.readline().rstrip())
index_range = range(0, N)
graph = []
visited = [[False for _ in range(N)] for _ in range(N)]
for i in range(N):
    graph.append(list(map(int, sys.stdin.readline().rstrip())))
    
answer = 0
nov_mem = []
for i in range(N):
    for j in range(N):
        if graph[i][j] == 1 and dfs(i, j) == True:
            answer += 1
            nov_mem.append(nov)
            nov = 0

print(answer)
nov_mem = sorted(nov_mem)
for nov in nov_mem:
    print(nov)