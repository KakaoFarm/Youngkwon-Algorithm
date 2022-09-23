#
# Baekjoon 14502 - 연구소
# Gold 4
# 그래프 이론, BFS, 브루트포스
#

import sys
from copy import deepcopy
from collections import deque
from itertools import combinations
input = sys.stdin.readline


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
N, M = map(int, input().split())
original = []
empty = []
virus = []
for i in range(N):
    row = list(map(int, input().split()))
    original.append(row)
    for j in range(M):
        if row[j] == 0:
            empty.append((i, j))
        elif row[j] == 2:
            virus.append((i, j))


def bfs():
    global count
    q = deque(virus)
    while q:
        i, j = q.popleft()
        for k in range(4):
            ni = i + dx[k]
            nj = j + dy[k]
            if ni in range(N) and nj in range(M) and _map[ni][nj] == 0:
                _map[ni][nj] = 2
                count -= 1
                q.append((ni, nj))


answer = -1
comb = combinations(empty, 3)
for c in comb:
    count = len(empty) - 3
    _map = deepcopy(original)
    for x, y in c:
        _map[x][y] = 1
    bfs()
    answer = max(answer, count)

print(answer)
