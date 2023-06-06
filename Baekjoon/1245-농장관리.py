#
# Baekjoon 1245 - 농장 관리
# Gold 5
# 그래프 탐색
#


import sys
from collections import deque
input = sys.stdin.readline

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]
tidx = 0
board = []
n, m = 0, 0

def check_top(_i, _j):
    global tidx
    height = board[_i][_j]
    q = deque()
    q.append((_i, _j, height))
    pos_list = [(_i, _j)]
    is_top = True
    while q:
        i, j, h = q.popleft()
        for d in range(8):
            ni = i + dx[d]
            nj = j + dy[d]
            if ni in range(n) and nj in range(m):
                if board[ni][nj] > h or board[ni][nj] < 0:
                    is_top = False
                    break
                elif board[ni][nj] == h and (ni, nj) not in pos_list:
                    pos_list.append((ni, nj))
                    q.append((ni, nj, h))
    if is_top:
        tidx -= 1
        for i, j in pos_list:
            board[i][j] = tidx
    

def main():
    global board, n, m
    n, m = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]

    for i in range(n):
        for j in range(m):
            if board[i][j] > 0:
                check_top(i, j)
    print(-tidx)

main()