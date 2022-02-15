#
# Baekjoon 1523 - 퍼즐
# Gold 2
# 그래프 이론, 자료구조
#

import sys
from collections import deque
input = sys.stdin.readline
answer = '123456780'
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def swap(puzzle, pos_a, pos_b):
    char_a = puzzle[pos_a]
    char_b = puzzle[pos_b]
    puzzle = puzzle[:pos_b] + char_a + puzzle[pos_b+1:]
    puzzle = puzzle[:pos_a] + char_b + puzzle[pos_a+1:]
    return puzzle


def bfs(str_puzzle):
    q = deque()
    q.append((str_puzzle, 0))
    visited[str_puzzle] = 1

    while q:
        (puzzle, move_count) = q.popleft()

        # Answer랑 같은 puzzle 배치
        if puzzle == answer:
            return move_count

        pos = puzzle.find('0')
        row = pos // 3
        col = pos % 3

        for k in range(4):
            new_row = row + dx[k]
            new_col = col + dy[k]
            if new_row in range(3) and new_col in range(3):
                new_puzzle = puzzle
                new_puzzle = swap(new_puzzle, pos, new_row*3 + new_col)
                if not visited.get(new_puzzle):
                    visited[new_puzzle] = 1
                    q.append((new_puzzle, move_count + 1))
    return -1


visited = {}
str_puzzle = ""
for _ in range(3):
    temp_list = list(map(int, input().split()))
    str_puzzle += str(temp_list[0]) + str(temp_list[1]) + str(temp_list[2])
print(bfs(str_puzzle))
