#
# Baekjoon 19238 - 스타트 택시
# Gold 2
# 그래프 이론
#

import sys
from heapq import heappush, heappop
from queue import deque
from copy import deepcopy
input = sys.stdin.readline
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(a, b, c, d):
    q = deque([(a, b, 0)])
    visited = [[False for _ in range(N + 1)] for _ in range(N + 1)]
    while q:
        x, y, dist = q.popleft()
        visited[x][y] = True
        if (x, y) == (c, d):
            return dist
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx in range(1, N + 1) and ny in range(1, N + 1) and _map[nx][ny] == 0 and not visited[nx][ny]:
                q.append((nx, ny, dist + 1))


N, M, P = map(int, input().split())
_map = [[1 for _ in range(N + 1)]]
for _ in range(N):
    _map.append([1] + list(map(int, input().split())))
curr_x, curr_y = map(int, input().split())
_pos = [list(map(int, input().split())) for _ in range(M)]
pos = []
for i in range(len(_pos)):
    d = bfs(curr_x, curr_y, _pos[i][0], _pos[i][1])
    heappush(pos, [d] + _pos[i])

while len(pos) > 0:
    dist1, start_x, start_y, end_x, end_y = heappop(pos)
    if dist1 == None:
        P = -1
        break
    P -= dist1
    if P < 0:
        P = -1
        break
    dist2 = bfs(start_x, start_y, end_x, end_y)
    P -= dist2
    if P < 0:
        P = -1
        break
    else:
        P += dist2 * 2
        curr_x, curr_y = end_x, end_y
        temp = []
        while pos:
            d, sx, sy, ex, ey = heappop(pos)
            heappush(temp, [bfs(curr_x, curr_y, sx, sy), sx, sy, ex, ey])
        pos = deepcopy(temp)

print(P)
