#
# Baekjoon 1937 - 욕심쟁이 판다
# Gold 3
# 그래프 이론, 다이나믹 프로그래밍
#

import sys
sys.setrecursionlimit(10**9)
def input(): return sys.stdin.readline().rstrip()


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def dfs(x, y):
    if dp[x][y] == -1:
        max_depth = 0
        for i in range(4):
            new_x = x + dx[i]
            new_y = y + dy[i]
            if new_x in index_range and new_y in index_range:
                if graph[new_x][new_y] > graph[x][y]:
                    dep = dfs(new_x, new_y)
                    max_depth = max(max_depth, dep)

        if max_depth == 0:
            dp[x][y] = 1
        else:
            dp[x][y] = max_depth + 1

    return dp[x][y]


N = int(input())
index_range = range(N)
graph = []
dp = [[-1 for _ in range(N)] for _ in range(N)]
for _ in range(N):
    graph.append(list(map(int, input().split())))

for i in range(N):
    for j in range(N):
        if dp[i][j] == -1:
            dfs(i, j)

answer = 0
for row in dp:
    answer = max(answer, max(row))
print(answer)
