#
# Baekjoon 17143 - 낚시왕
# Gold 2
# 구현, 시뮬레이션
#

import sys
input = sys.stdin.readline


def catch(board, col):
    for row in range(1, len(board)):
        if board[row][col] != 0:
            return (row, col)
    return False


def get_arrive_position(s, d, row, col, max_row, max_col):
    if d == 1:  # UP
        row -= s
    elif d == 2:  # DOWN
        row += s
    elif d == 3:  # RIGHT
        col += s
    elif d == 4:  # LEFT
        col -= s

    while row not in range(1, max_row+1):
        if row < 1:
            row = 1 + (1 - row)
            d = 2
        if row > max_row:
            row = max_row - (row - max_row)
            d = 1
    while col not in range(1, max_col+1):
        if col < 1:
            col = 1 + (1 - col)
            d = 3
        if col > max_col:
            col = max_col - (col - max_col)
            d = 4

    return (row, col, d)


def shark_move(old_board, sharks):
    new_board = [[False for _ in range(len(old_board[0]))]
                 for _ in range(len(old_board))]

    for shark_index in range(1, len(sharks)):
        r, c, s, d, z = sharks[shark_index]
        if r == -1 and c == -1:
            continue
        new_r, new_c, d = get_arrive_position(
            s, d, r, c, len(old_board)-1, len(old_board[0])-1)
        if new_board[new_r][new_c] == False:
            sharks[shark_index] = (new_r, new_c, s, d, z)
            new_board[new_r][new_c] = shark_index
        else:
            target_index = new_board[new_r][new_c]
            if sharks[target_index][4] < sharks[shark_index][4]:
                sharks[target_index] = (-1, -1, -1, -1, -1)
                sharks[shark_index] = (new_r, new_c, s, d, z)
                new_board[new_r][new_c] = shark_index
            else:
                sharks[shark_index] = (-1, -1, -1, -1, -1)
    return (new_board, sharks)


def solution():
    answer = 0
    R, C, M = map(int, input().split())
    board = [[False for _ in range(C+1)] for _ in range(R+1)]
    sharks = [(-1, -1, -1, -1, -1)]

    for shark_index in range(1, M+1):
        r, c, s, d, z = map(int, input().split())
        board[r][c] = shark_index
        sharks.append((r, c, s, d, z))

    for pos in range(1, C+1):
        _catch = catch(board, pos)
        if _catch != False:
            r, c = _catch
            r, c, s, d, z = sharks[board[r][c]]
            answer += z
            sharks[board[r][c]] = (-1, -1, -1, -1, -1)
            board[r][c] = False

        board, sharks = shark_move(board, sharks)
    return answer


print(solution())
