# 
# Baekjoon 10026 - 적록색약
# Gold 5
# 그래프 이론
# 

import sys
sys.setrecursionlimit(10**6)

def DFS(i, j, rg_person):
    index_range = range(0, N)
    # Index range 체크
    if i not in index_range or j not in index_range:
        return False
      
    # 방문 여부 체크
    if visited[i][j] == True:
        return False
    # 방문 처리  
    visited[i][j] = True
    
    color = graph[i][j]
    
    # 적록 색약이 아니면 정상적인 DFS 수행
    if rg_person == False:
        if (i-1) in index_range and graph[i-1][j] == color:
            DFS(i-1, j, rg_person)
        if (i+1) in index_range and graph[i+1][j] == color:
            DFS(i+1, j, rg_person)
        if (j-1) in index_range and graph[i][j-1] == color:
            DFS(i, j-1, rg_person)
        if (j+1) in index_range and graph[i][j+1] == color:
            DFS(i, j+1, rg_person)
    
    # 적록 색약이라면 적록색약 DFS 수행
    if rg_person == True:
        color_range = ['R', 'G']
        if color in color_range:
            if (i-1) in index_range and graph[i-1][j] in color_range:
                DFS(i-1, j, rg_person)
            if (i+1) in index_range and graph[i+1][j] in color_range:
                DFS(i+1, j, rg_person)
            if (j-1) in index_range and graph[i][j-1] in color_range:
                DFS(i, j-1, rg_person)
            if (j+1) in index_range and graph[i][j+1] in color_range:
                DFS(i, j+1, rg_person) 
        else:
            if (i-1) in index_range and graph[i-1][j] == color:
                DFS(i-1, j, rg_person)
            if (i+1) in index_range and graph[i+1][j] == color:
                DFS(i+1, j, rg_person)
            if (j-1) in index_range and graph[i][j-1] == color:
                DFS(i, j-1, rg_person)
            if (j+1) in index_range and graph[i][j+1] == color:
                DFS(i, j+1, rg_person)
    
    return True
    
N = int(sys.stdin.readline().rstrip())
graph = []
for i in range(N):
    graph.append(list(sys.stdin.readline().rstrip()))
    
    
answer = [0, 0]
visited = [[False for _ in range(N)] for _ in range(N)]
for i in range(N):
    for j in range(N):
        if DFS(i, j, False) == True:
            answer[0] += 1

visited = [[False for _ in range(N)] for _ in range(N)]
for i in range(N):
    for j in range(N):
        if DFS(i, j, True) == True:
            answer[1] += 1

print(answer[0], answer[1])