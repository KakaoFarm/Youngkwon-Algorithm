#
# Baekjoon 2178 - 미로 탐색
# Silver 1
# 그래프 이론
#

import sys
from collections import deque
input = sys.stdin.readline
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs():
    visited = [[-1 for _ in range(M)] for _ in range(N)]
    q = deque()
    q.append((0, 0))
    visited[0][0] = 1
    while q:
        x, y = q.popleft()
        if x == N-1 and y == M-1:
            return visited[x][y]
        for i in range(4):
            new_x = x + dx[i]
            new_y = y + dy[i]
            if (new_x in x_range and new_y in y_range) and visited[new_x][new_y] == -1 and graph[new_x][new_y] == 1:
                visited[new_x][new_y] = visited[x][y] + 1
                q.append((new_x, new_y))


N, M = map(int, input().split())
graph = []
for _ in range(N):
    graph.append(list(map(int, list(input().rstrip()))))
x_range = range(N)
y_range = range(M)
print(bfs())
