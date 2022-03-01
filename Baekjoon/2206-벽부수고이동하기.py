#
# Baekjoon 2206 - 벽 부수고 이동하기
# Gold 4
# 그래프 이론, BFS
#

import sys
from collections import deque
input = sys.stdin.readline
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs():
    q = deque()
    visited = [[[0, 0] for _ in range(M)] for _ in range(N)]
    visited[0][0][1] = 1
    q.append((0, 0, 1))  # n, m, can_crash
    while q:
        n, m, crash = q.popleft()
        if n == N-1 and m == M-1:
            return visited[n][m][crash]
        for i in range(4):
            new_n = n + dx[i]
            new_m = m + dy[i]
            if new_n in n_range and new_m in m_range:
                if graph[new_n][new_m] == 1 and crash == 1:
                    visited[new_n][new_m][0] = visited[n][m][1] + 1
                    q.append((new_n, new_m, 0))
                elif graph[new_n][new_m] == 0 and visited[new_n][new_m][crash] == 0:
                    visited[new_n][new_m][crash] = visited[n][m][crash] + 1
                    q.append((new_n, new_m, crash))
    return -1


N, M = map(int, input().split())
n_range = range(N)
m_range = range(M)
graph = []

for _ in range(N):
    graph.append(list(map(int, list(input().rstrip()))))

answer = bfs()
print(answer)
