#
# Baekjoon 19236 - 청소년 상어
# Gold 2
# 구현, 백트래킹
#

import copy
from queue import deque

pos = [[0, 0] for _ in range(17)]
board = [[] for _ in range(4)]
dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]
for i in range(4):
    a, b, c, d, e, f, g, h = map(int, input().split())
    board[i].append([a, b-1])
    board[i].append([c, d-1])
    board[i].append([e, f-1])
    board[i].append([g, h-1])
    pos[a] = [i, 0]
    pos[c] = [i, 1]
    pos[e] = [i, 2]
    pos[g] = [i, 3]


def fish_move(_board, _pos):
    for fish_num in range(1, 17):
        if _pos[fish_num] == False:
            continue
        curr_i, curr_j = _pos[fish_num]

        for offset in range(8):
            direction = (_board[curr_i][curr_j][1] + offset) % 8
            new_i, new_j = curr_i + dx[direction], curr_j + dy[direction]
            if new_i in range(4) and new_j in range(4) and _board[new_i][new_j][0] != -1:
                if _board[new_i][new_j][0] == 0:  # 빈 공간으로 이동
                    _board[new_i][new_j] = _board[curr_i][curr_j]
                    _board[new_i][new_j][1] = direction
                    _board[curr_i][curr_j] = [0, 0]
                    _pos[_board[new_i][new_j][0]] = [new_i, new_j]

                elif _board[new_i][new_j][0] in range(1, 17):  # 물고기와 위치 변경
                    _board[new_i][new_j], _board[curr_i][curr_j] = _board[curr_i][curr_j], _board[new_i][new_j]
                    _board[new_i][new_j][1] = direction
                    _pos[_board[new_i][new_j][0]] = [new_i, new_j]
                    _pos[_board[curr_i][curr_j][0]] = [curr_i, curr_j]

                break

    return _board, _pos


answer = 0
q = deque([(0, 0, 0, 0, board, pos, [])])
while q:
    old_shark_i, old_shark_j, shark_i, shark_j, _board, _pos, eat = q.popleft()
    if (old_shark_i, old_shark_j) != (shark_i, shark_j):
        _board[old_shark_i][old_shark_j] = [0, 0]
    eat_fish_num = _board[shark_i][shark_j][0]
    _pos[eat_fish_num] = False
    _board[shark_i][shark_j][0] = -1
    shark_direction = _board[shark_i][shark_j][1]
    eat.append(eat_fish_num)
    answer = max(answer, sum(eat))
    _board, _pos = fish_move(_board, _pos)

    for step in range(1, 4):
        new_shark_i = shark_i + (dx[shark_direction] * step)
        new_shark_j = shark_j + (dy[shark_direction] * step)

        if new_shark_i not in range(4) or new_shark_j not in range(4):
            break

        if _board[new_shark_i][new_shark_j][0] in range(1, 17):

            new_board = copy.deepcopy(_board)
            new_pos = []
            for row in _pos:
                new_pos.append(row)
            q.append((shark_i, shark_j, new_shark_i, new_shark_j, new_board,
                     new_pos, eat))

print(answer)
