#
# Baekjoon 9328 - 열쇠
# Gold 1
# 그래프 이론, BFS
#

import sys
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

input = sys.stdin.readline
T = int(input())


def unlock(k):
    for r in range(row):
        for c in range(col):
            if graph[r][c] == k or graph[r][c] == k.upper():
                graph[r][c] = '.'


def init_start():
    d = 0
    result = []
    for c in range(col):
        if graph[0][c] != '*' and not graph[0][c].isupper():
            if graph[0][c] == '$':
                d += 1
            visited[0][c] = True
            result.append((0, c))
        if graph[row - 1][c] != '*' and not graph[row - 1][c].isupper():
            if graph[row - 1][c] == '$':
                d += 1
            visited[row - 1][c] = True
            result.append((row - 1, c))

    for r in range(1, row - 1):
        if graph[r][0] != '*' and not graph[r][0].isupper():
            if graph[r][0] == '$':
                d += 1
            visited[r][0] = True
            result.append((r, 0))
        if graph[r][col - 1] != '*' and not graph[r][col - 1].isupper():
            if graph[r][col - 1] == '$':
                d += 1
            visited[r][col - 1] = True
            result.append((r, col - 1))
    return (d, result)


for _ in range(T):
    graph = []
    row, col = map(int, input().split())
    visited = [[False for j in range(col)] for i in range(row)]
    for r in range(row):
        graph.append(list(input()))
    for k in list(input()):
        if k != "0":
            unlock(k)
    docs, lst = init_start()
    q = deque(lst)
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx in range(row) and ny in range(col) and not visited[nx][ny]:
                if graph[nx][ny] == '.':
                    q.append((nx, ny))
                    visited[nx][ny] = True
                elif graph[nx][ny] == '$':
                    q.append((nx, ny))
                    visited[nx][ny] = True
                    docs += 1
                elif graph[nx][ny] != '*' and not graph[nx][ny].isupper():
                    unlock(graph[nx][ny])
                    visited = [
                        [False for j in range(col)] for i in range(row)]
                    docs, lst = init_start()
                    q = deque(lst)

    print(docs)
