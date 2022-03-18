#
# Baekjoon 9376 - 탈옥
# Gold 3
# 그래프 이론
#

import sys
from collections import deque
input = sys.stdin.readline
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


T = int(input())
graph = []
_x1, _y1 = (0, 0)
_x2, _y2 = (0, 0)


def escape(_x, _y):
    global height, width
    q = deque()
    q.append((_x, _y, []))  # x, y, open한 문의 좌표
    visited = [[False for _ in range(width)] for _ in range(height)]
    visited[_x][_y] = True
    while q:
        x, y, door_list = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            # 탈출 성공
            if nx not in range(0, height) or ny not in range(0, width):
                return door_list

            if (graph[nx][ny] == 0 or graph[nx][ny] == 2) and visited[nx][ny] == False:
                visited[nx][ny] = True
                q.appendleft((nx, ny, door_list))

            if graph[nx][ny] == 1 and visited[nx][ny] == False:
                visited[nx][ny] = True
                q.append((nx, ny, door_list + [(nx, ny)]))
    return False


for _ in range(T):
    first = True
    height, width = map(int, input().split())
    for k in range(height):
        row = []
        _input = list(input().rstrip())
        for h in range(width):
            char = _input[h]
            # space
            if char == '.':
                row.append(0)
            # door
            elif char == '#':
                row.append(1)
            # member
            elif char == '$':
                row.append(2)
                if first:
                    first = False
                    _x1, _y1 = k, h
                else:
                    _x2, _y2 = k, h
            # wall
            elif char == '*':
                row.append(3)
        graph.append(row)

    result_1, result_2 = False, False
    while not result_1 and not result_2:
        result_1 = escape(_x1, _y1)
        if result_1 != False:
            graph[_x1][_y1] = 0
        result_2 = escape(_x2, _y2)
        if result_2 != False:
            graph[_x2][_y2] = 0
    print(len(result_1) + len(result_2))
