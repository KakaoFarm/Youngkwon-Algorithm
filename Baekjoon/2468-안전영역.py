#
# Baekjoon 2468 - 안전 영역
# Silver 1
# 브루트포스, 그래프탐색
#

import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def dfs(i, j, rain):
    dead[i][j] = False
    for k in range(4):
        new_i = i + dx[k]
        new_j = j + dy[k]
        if new_i in index_range and new_j in index_range and graph[new_i][new_j] > rain and dead[new_i][new_j]:
            dfs(new_i, new_j, rain)


N = int(input())
index_range = range(N)
_max = 0
graph = []
for _ in range(N):
    _list = list(map(int, input().split()))
    _max = max(_max, max(_list))
    graph.append(_list)


answer = 0
safe_area = 0
for rain in range(0, _max):
    answer = max(answer, safe_area)
    safe_area = 0
    dead = [[True for _ in range(N)] for _ in range(N)]
    for i in range(0, N):
        for j in range(0, N):
            if graph[i][j] > rain and dead[i][j]:
                safe_area += 1
                dfs(i, j, rain)
answer = max(answer, safe_area)
print(answer)
