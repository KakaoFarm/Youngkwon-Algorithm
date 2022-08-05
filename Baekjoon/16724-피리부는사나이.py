#
# Baekjoon 16724 - 피리 부는 사나이
# Gold 3
# 그래프 이론, 자료구조
#

import sys
input = sys.stdin.readline


def dfs(row, col, dfs_index):
    global safezone
    visited[row][col] = dfs_index

    if graph[row][col] == 'U':
        if visited[row - 1][col] == -1:
            dfs(row - 1, col, dfs_index)
        elif visited[row - 1][col] == dfs_index:
            safezone += 1

    elif graph[row][col] == 'D':
        if visited[row + 1][col] == -1:
            dfs(row + 1, col, dfs_index)
        elif visited[row + 1][col] == dfs_index:
            safezone += 1

    elif graph[row][col] == 'L':
        if visited[row][col - 1] == -1:
            dfs(row, col - 1, dfs_index)
        elif visited[row][col - 1] == dfs_index:
            safezone += 1

    elif graph[row][col] == 'R':
        if visited[row][col + 1] == -1:
            dfs(row, col + 1, dfs_index)
        elif visited[row][col + 1] == dfs_index:
            safezone += 1


N, M = map(int, input().split())
graph = []
safezone = 0
visited = [[-1 for i in range(M)] for j in range(N)]
for _ in range(N):
    graph.append(list(input()))

dfs_index = 0
for row in range(N):
    for col in range(M):
        if visited[row][col] == -1:
            dfs(row, col, dfs_index)
            dfs_index += 1

print(safezone)
