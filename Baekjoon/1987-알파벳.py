#
# Baekjoon 1987 - 알파벳
# Gold 4
# 그래프 이론
#

import sys
input = sys.stdin.readline
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def dfs(x, y, depth):
    global _max
    _max = max(_max, depth)
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx in x_range and ny in y_range and graph[nx][ny] and check[ord(graph[nx][ny]) - 65] == 0:
            check[ord(graph[nx][ny]) - 65] = 1
            dfs(nx, ny, depth + 1)
            check[ord(graph[nx][ny]) - 65] = 0


R, C = map(int, input().split())
graph = []
x_range = range(R)
y_range = range(C)
for _ in range(R):
    graph.append(list(input()))

_max = 0
check = [0]*(26)
check[ord(graph[0][0]) - 65] = 1
dfs(0, 0, 1)
print(_max)
