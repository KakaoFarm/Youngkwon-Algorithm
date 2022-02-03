# 
# Baekjoon 2667 - 단지번호붙이기
# Gold 5
# 그래프 이론, BFS
# 

import sys
from collections import deque

def bfs():
    queue = deque([])
    for h in range(H):
        for n in range(N):
            for m in range(M):
                if graph[h][n][m] == 1:
                    queue.append((h, n, m))

    while queue:
        (h, n, m) = queue.popleft()
        for i in range(6):
            new_h = h + dh[i]
            new_n = n + dn[i]
            new_m = m + dm[i]
            
            if new_h in range_h and new_n in range_n and new_m in range_m:
                if graph[new_h][new_n][new_m] == 0:
                    graph[new_h][new_n][new_m] = graph[h][n][m] + 1
                    queue.append((new_h, new_n, new_m))


(M, N, H) = map(int, sys.stdin.readline().rstrip().split())

dh = [-1, 1, 0, 0, 0, 0]
dn = [0, 0, -1, 1, 0, 0]
dm = [0, 0, 0, 0, -1, 1]

range_h = range(0, H)
range_n = range(0, N)
range_m = range(0, M)

graph = [] # graph[H][row: N][col: M]

for i in range(H):
    board = []
    for j in range(N):
        board.append(list(map(int, sys.stdin.readline().rstrip().split())))
    graph.append(board)

bfs()
max_day = 0
for h in range(H):
    if max_day == -1:
        break
    for n in range(N):
        if max_day == -1:
            break
        for m in range(M):
            # 안익은 토마토 발견
            if graph[h][n][m] == 0:
                max_day = -1
                break
            max_day = max(max_day, graph[h][n][m])
            
if max_day == -1:
    print(-1)
else:
    print(max_day - 1)