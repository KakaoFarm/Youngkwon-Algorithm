#
# Baekjoon 19236 - 청소년 상어
# Gold 2
# 구현, 백트래킹
#

import copy

board = [[] for _ in range(4)]
dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]
answer = 0

for i in range(4):
    a, b, c, d, e, f, g, h = map(int, input().split())
    board[i].append([a, b-1])
    board[i].append([c, d-1])
    board[i].append([e, f-1])
    board[i].append([g, h-1])


def dfs(sx, sy, eat, board):
    global answer
    eat += board[sx][sy][0]
    answer = max(answer, eat)
    board[sx][sy][0] = 0

    # 물고기 움직임
    for fish_num in range(1, 17):
        fx, fy = -1, -1
        for i in range(4):
            for j in range(4):
                if board[i][j][0] == fish_num:
                    fx, fy = i, j
                    break

        if (fx, fy) == (-1, -1):
            continue
        fd = board[fx][fy][1]

        for offset in range(8):
            nd = (fd + offset) % 8
            nx = fx + dx[nd]
            ny = fy + dy[nd]
            if nx not in range(4) or ny not in range(4) or (nx == sx and ny == sy):
                continue
            board[fx][fy][1] = nd
            board[nx][ny], board[fx][fy] = board[fx][fy], board[nx][ny]
            break

    # 상어 움직임
    sd = board[sx][sy][1]
    for i in range(1, 4):
        nx = sx + (dx[sd] * i)
        ny = sy + (dy[sd] * i)

        if nx in range(4) and ny in range(4) and board[nx][ny][0] > 0:
            temp_board = copy.deepcopy(board)
            dfs(nx, ny, eat, temp_board)


dfs(0, 0, 0, board)
print(answer)
