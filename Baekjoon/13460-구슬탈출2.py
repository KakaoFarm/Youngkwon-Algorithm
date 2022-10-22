#
# Baekjoon 13460 - 구슬 탈출 2
# Gold 1
# 구현, 그래프 이론
#

from queue import deque

n, m = 0, 0
n_limit, m_limit = range(n), range(m)
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


def left_move(_board):
    board = [each[:] for each in _board]
    red_succeed, blue_succeed = False, False
    for i in range(1, n-1):
        for j in range(1, m-1):
            if board[i][j] in ['R', 'B']:
                temp_i, temp_j = i, j
                while True:
                    ni = temp_i + dx[0]
                    nj = temp_j + dy[0]
                    if ni not in n_limit or nj not in m_limit or board[ni][nj] in ['#', 'R', 'B']:
                        break

                    if board[ni][nj] == 'O':
                        if board[temp_i][temp_j] == 'R':
                            board[temp_i][temp_j] = '.'
                            red_succeed = True
                            break
                        elif board[temp_i][temp_j] == 'B':
                            board[temp_i][temp_j] = '.'
                            blue_succeed = True
                            break
                    board[ni][nj], board[temp_i][temp_j] = board[temp_i][temp_j], board[ni][nj]
                    temp_i, temp_j = ni, nj

    if blue_succeed:
        return board, False
    elif red_succeed:
        return board, True
    return board, None


def right_move(_board):
    board = [each[:] for each in _board]
    red_succeed, blue_succeed = False, False
    for i in range(1, n-1):
        for j in range(m-2, 0, -1):
            if board[i][j] in ['R', 'B']:
                temp_i, temp_j = i, j
                while True:
                    ni = temp_i + dx[1]
                    nj = temp_j + dy[1]
                    if ni not in n_limit or nj not in m_limit or board[ni][nj] in ['#', 'R', 'B']:
                        break

                    if board[ni][nj] == 'O':
                        if board[temp_i][temp_j] == 'R':
                            board[temp_i][temp_j] = '.'
                            red_succeed = True
                            break
                        elif board[temp_i][temp_j] == 'B':
                            board[temp_i][temp_j] = '.'
                            blue_succeed = True
                            break
                    board[ni][nj], board[temp_i][temp_j] = board[temp_i][temp_j], board[ni][nj]
                    temp_i, temp_j = ni, nj
    if blue_succeed:
        return board, False
    elif red_succeed:
        return board, True
    return board, None


def up_move(_board):
    board = [each[:] for each in _board]
    red_succeed, blue_succeed = False, False
    for i in range(1, n-1):
        for j in range(1, m-1):
            if board[i][j] in ['R', 'B']:
                temp_i, temp_j = i, j
                while True:
                    ni = temp_i + dx[2]
                    nj = temp_j + dy[2]
                    if ni not in n_limit or nj not in m_limit or board[ni][nj] in ['#', 'R', 'B']:
                        break

                    if board[ni][nj] == 'O':
                        if board[temp_i][temp_j] == 'R':
                            board[temp_i][temp_j] = '.'
                            red_succeed = True
                            break
                        elif board[temp_i][temp_j] == 'B':
                            board[temp_i][temp_j] = '.'
                            blue_succeed = True
                            break
                    board[ni][nj], board[temp_i][temp_j] = board[temp_i][temp_j], board[ni][nj]
                    temp_i, temp_j = ni, nj
    if blue_succeed:
        return board, False
    elif red_succeed:
        return board, True
    return board, None


def down_move(_board):
    board = [each[:] for each in _board]
    red_succeed, blue_succeed = False, False
    for i in range(n-2, 0, -1):
        for j in range(1, m-1):
            if board[i][j] in ['R', 'B']:
                temp_i, temp_j = i, j
                while True:
                    ni = temp_i + dx[3]
                    nj = temp_j + dy[3]
                    if ni not in n_limit or nj not in m_limit or board[ni][nj] in ['#', 'R', 'B']:
                        break

                    if board[ni][nj] == 'O':
                        if board[temp_i][temp_j] == 'R':
                            board[temp_i][temp_j] = '.'
                            red_succeed = True
                            break
                        elif board[temp_i][temp_j] == 'B':
                            board[temp_i][temp_j] = '.'
                            blue_succeed = True
                            break
                    board[ni][nj], board[temp_i][temp_j] = board[temp_i][temp_j], board[ni][nj]
                    temp_i, temp_j = ni, nj
    if blue_succeed:
        return board, False
    elif red_succeed:
        return board, True
    return board, None


def main():
    global n, m, n_limit, m_limit
    n, m = map(int, input().split())
    n_limit, m_limit = range(n), range(m)
    answer = -1
    _board = []
    for _ in n_limit:
        _board.append(list(input()))

    q = deque([(_board, 0)])
    visited = []
    while q:
        board, move = q.popleft()
        visited.append(board)
        if move > 10:
            break

        # left move
        moved_board, succeed = left_move(board)
        if succeed:
            answer = move+1
            break
        if succeed == None and moved_board != board and moved_board not in visited:
            q.append((moved_board, move+1))

        # right move
        moved_board, succeed = right_move(board)
        if succeed:
            answer = move+1
            break
        if succeed == None and moved_board != board and moved_board not in visited:
            q.append((moved_board, move+1))

        # up move
        moved_board, succeed = up_move(board)
        if succeed:
            answer = move+1
            break
        if succeed == None and moved_board != board and moved_board not in visited:
            q.append((moved_board, move+1))

        # down move
        moved_board, succeed = down_move(board)
        if succeed:
            answer = move+1
            break
        if succeed == None and moved_board != board and moved_board not in visited:
            q.append((moved_board, move+1))

    if answer <= 10:
        print(answer)
    else:
        print(-1)


main()
