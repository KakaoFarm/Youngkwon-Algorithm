#
# Baekjoon 16236 - 아기상어
# Gold 3
# 그래프 이론
#

import sys
from collections import deque
from queue import PriorityQueue
input = sys.stdin.readline
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]


def get_target_position(pos_i, pos_j):
    q = deque([])
    q.append((pos_i, pos_j))
    visited = [[-1 for _ in range(N)] for _ in range(N)]
    visited[pos_i][pos_j] = 0
    _mem = PriorityQueue()

    while q:
        curr_i, curr_j = q.popleft()
        for i in range(4):
            new_i = curr_i + dx[i]
            new_j = curr_j + dy[i]
            if new_i in range(N) and new_j in range(N) and graph[new_i][new_j] <= size and visited[new_i][new_j] == -1:
                visited[new_i][new_j] = visited[curr_i][curr_j] + 1
                q.append((new_i, new_j))
                if graph[new_i][new_j] != 0 and graph[new_i][new_j] != size:
                    _mem.put((visited[new_i][new_j], new_i, new_j))
    if _mem.qsize() > 0:
        return _mem.get()
    return (-1, -1, -1)


N = int(input())
graph = []
(pos_i, pos_j, size, time, eat) = (0, 0, 2, 0, 0)
for i in range(N):
    row = list(map(int, input().split()))
    graph.append(row)
    if 9 in row:
        pos_i = i
        pos_j = row.index(9)


while True:
    move_time, target_i, target_j = get_target_position(pos_i, pos_j)
    if target_i == -1:
        break
    graph[pos_i][pos_j] = 0
    (pos_i, pos_j) = (target_i, target_j)
    graph[target_i][target_j] = 9
    time += move_time
    eat += 1
    if eat == size:
        eat = 0
        size += 1

print(time)
