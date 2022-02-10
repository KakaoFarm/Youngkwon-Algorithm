#
# Baekjoon 2338 - 치즈
# Gold 4
# 그래프 이론, 구현
#

import sys
from collections import deque
def input(): return sys.stdin.readline().rstrip()


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def anHourBFS():
    q = deque()
    q.append((0, 0))
    visited = [[0 for _ in range(COL)] for _ in range(ROW)]
    visited[0][0] = 2
    melt_count = 0
    while q:
        (row, col) = q.popleft()
        for i in range(4):
            new_row = row + dx[i]
            new_col = col + dy[i]
            if new_row in range(0, ROW) and new_col in range(0, COL) and (visited[new_row][new_col] != 2):
                if graph[new_row][new_col] == 1:
                    if visited[new_row][new_col] == 1:  # 2번째로 공기와 마찰
                        graph[new_row][new_col] = 0
                        visited[new_row][new_col] = 2
                        melt_count += 1
                    else:
                        visited[new_row][new_col] = 1
                else:
                    visited[new_row][new_col] = 2
                    q.append((new_row, new_col))
    return melt_count


(ROW, COL) = map(int, input().split())
graph = []
for _ in range(ROW):
    graph.append(list(map(int, input().split())))

time = 0
while True:
    melt_count = anHourBFS()
    if melt_count == 0:
        print(time)
        break
    time += 1
