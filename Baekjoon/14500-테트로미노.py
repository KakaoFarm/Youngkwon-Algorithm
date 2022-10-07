#
# Baekjoon 14500 - 테트로미노
# Gold 4
# 구현
#

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
row_range = range(N)
col_range = range(M)
board = [list(map(int, input().split())) for _ in range(N)]
blocks = [
    [(0, 0), (0, 1), (0, 2), (0, 3)],
    [(0, 0), (1, 0), (2, 0), (3, 0)],
    # ----
    [(0, 0), (0, 1), (1, 0), (1, 1)],
    # ----
    [(0, 0), (1, 0), (2, 0), (2, 1)],
    [(0, 0), (1, 0), (2, 0), (2, -1)],
    [(0, 0), (0, 1), (0, 2), (1, 2)],
    [(0, 0), (0, -1), (0, -2), (1, -2)],
    [(0, 0), (1, 0), (1, 1), (1, 2)],
    [(0, 0), (1, 0), (1, -1), (1, -2)],
    [(0, 0), (0, 1), (1, 1), (2, 1)],
    [(0, 0), (0, -1), (1, -1), (2, -1)],
    # ----
    [(0, 0), (1, 0), (1, 1), (2, 1)],
    [(0, 0), (1, 0), (1, -1), (2, -1)],
    [(0, 0), (0, 1), (1, 1), (1, 2)],
    [(0, 0), (0, -1), (1, -1), (1, -2)],
    # ----
    [(0, 0), (0, 1), (0, 2), (1, 1)],
    [(0, 0), (1, 0), (1, 1), (2, 0)],
    [(0, 0), (1, 0), (1, -1), (2, 0)],
    [(0, 0), (1, -1), (1, 0), (1, 1)],
]


def get_max_point(i, j):
    max_point = 0
    for block in blocks:
        point = 0
        flag = True
        for dx, dy in block:
            if i + dx in row_range and j + dy in col_range:
                point += board[i + dx][j + dy]
            else:
                flag = False
                break
        if flag:
            max_point = max(max_point, point)
    return max_point


answer = 0
for i in row_range:
    for j in col_range:
        answer = max(answer, get_max_point(i, j))
print(answer)
