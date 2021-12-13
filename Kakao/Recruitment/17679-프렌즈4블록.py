global answer, nor, noc
answer = 0


def solution(m, n, board):
    global answer, nor, noc
    nor = m
    noc = n
    board = [list(r) for r in board]
    recursive(board)
    answer = get_answer(board)
    return answer


def recursive(board):
    rec = False
    for i in range(nor-1):
        for k in range(noc-1):
            spot = board[i][k][0]
            if spot != "_" and (spot == board[i][k+1][0] and spot == board[i+1][k][0] and spot == board[i+1][k+1][0]):
                mark__(board, i, k)
                rec = True
    fall(board)
    if(rec):
        recursive(board)
    return


def mark__(board, left_top_row, left_top_col):
    board[left_top_row][left_top_col] += '_'
    board[left_top_row][left_top_col+1] += '_'
    board[left_top_row+1][left_top_col] += '_'
    board[left_top_row+1][left_top_col+1] += '_'


def fall(board):
    global answer
    for i in range(nor-2, -1, -1):
        for k in range(noc):
            if "_" in board[i+1][k]:
                target_row = -1
                for t in range(i, -1, -1):
                    if "_" not in board[t][k]:
                        target_row = t
                        (board[target_row][k], board[i+1][k]
                         ) = (board[i+1][k], board[target_row][k])
                        break

    for i in range(nor):
        for k in range(noc):
            if len(board[i][k]) != 1:
                answer += 1
                board[i][k] = "_"


def get_answer(board):
    answer = 0
    for row in board:
        for e in row:
            if e == "_":
                answer += 1
    return answer
