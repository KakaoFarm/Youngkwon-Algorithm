#
# Baekjoon 16234 - 인구 이동
# Gold 5
# 그래프 이론, DFS
#

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)


def dfs(i, j, rec):
    global sum
    visited[i][j] = day
    sum += A[i][j]
    rec.append((i, j))
    for k in range(4):
        ni = i + dx[k]
        nj = j + dy[k]
        if ni in index and nj in index and visited[ni][nj] < day:
            diff = abs(A[ni][nj] - A[i][j])
            if diff <= R and diff >= L:
                dfs(ni, nj, rec)
    return rec


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

N, L, R = map(int, input().split())
index = range(N)

A = []
for _ in index:
    A.append(list(map(int, input().split())))

day = 0
sum = 0
visited = [[-1 for _ in index] for _ in index]

while True:
    mem = []
    for i in index:
        for j in index:
            if visited[i][j] == day:
                continue
            rec = dfs(i, j, [])
            if len(rec) > 1:
                mem.append((sum, rec))
            sum = 0

    if len(mem) == 0:
        break
    day += 1
    for s, rec in mem:
        for i, j in rec:
            A[i][j] = s // len(rec)

print(day)
