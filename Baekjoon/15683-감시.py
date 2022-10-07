#
# Baekjoon 15683 - 감시
# Gold 4
# 그래프 이론
#

import sys
from itertools import product
from copy import deepcopy
input = sys.stdin.readline


def get_answer():
    ans = 0
    for i in range(N):
        for j in range(M):
            if temp_map[i][j] == 0:
                ans += 1
    return ans


def left_visit(row, col):
    for c in range(col - 1, -1, -1):
        if temp_map[row][c] == 0:
            temp_map[row][c] = '#'
        if temp_map[row][c] == 6:
            break


def right_visit(row, col):
    for c in range(col + 1, M):
        if temp_map[row][c] == 0:
            temp_map[row][c] = '#'
        if temp_map[row][c] == 6:
            break


def up_visit(row, col):
    for r in range(row - 1, -1, -1):
        if temp_map[r][col] == 0:
            temp_map[r][col] = '#'
        if temp_map[r][col] == 6:
            break


def down_visit(row, col):
    for r in range(row + 1, N):
        if temp_map[r][col] == 0:
            temp_map[r][col] = '#'
        if temp_map[r][col] == 6:
            break


def set_cam(num, row, col, dic):
    if num == 1:
        if dic == 0:
            right_visit(row, col)

        elif dic == 1:
            up_visit(row, col)

        elif dic == 2:
            left_visit(row, col)

        elif dic == 3:
            down_visit(row, col)

    elif num == 2:
        if dic == 0:
            right_visit(row, col)
            left_visit(row, col)

        elif dic == 1:
            up_visit(row, col)
            down_visit(row, col)

    elif num == 3:
        if dic == 0:
            right_visit(row, col)
            up_visit(row, col)

        elif dic == 1:
            up_visit(row, col)
            left_visit(row, col)

        elif dic == 2:
            left_visit(row, col)
            down_visit(row, col)

        elif dic == 3:
            down_visit(row, col)
            right_visit(row, col)

    elif num == 4:
        if dic == 0:
            left_visit(row, col)
            right_visit(row, col)
            up_visit(row, col)

        elif dic == 1:
            up_visit(row, col)
            down_visit(row, col)
            left_visit(row, col)

        elif dic == 2:
            left_visit(row, col)
            right_visit(row, col)
            down_visit(row, col)

        elif dic == 3:
            up_visit(row, col)
            down_visit(row, col)
            right_visit(row, col)

    elif num == 5:
        up_visit(row, col)
        down_visit(row, col)
        left_visit(row, col)
        right_visit(row, col)


N, M = map(int, input().split())
board = []
cam = []  # num, row, col


for i in range(N):
    row = list(map(int, input().split()))
    for j in range(len(row)):
        elem = row[j]
        if elem != 6 and elem != 0:
            cam.append((elem, i, j))
    board.append(row)


cases = product([0, 1, 2, 3], repeat=len(cam))
possible_list = []
for case in list(cases):
    camera = []
    stop_flag = False
    for i in range(len(cam)):
        num, row, col = cam[i]
        if (num == 2 and case[i] in (2, 3)) or (num == 5 and case[i] in (1, 2, 3)):
            stop_flag = True
            break
        camera.append((num, row, col, case[i]))

    if stop_flag:
        continue
    possible_list.append(camera)


answer = float('inf')
for cam_list in possible_list:
    temp_map = deepcopy(board)

    for cam in cam_list:
        num, row, col, dic = cam
        set_cam(num, row, col, dic)
    answer = min(answer, get_answer())
print(answer)
