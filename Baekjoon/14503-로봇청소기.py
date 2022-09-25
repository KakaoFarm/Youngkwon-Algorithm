#
# Baekjoon 14503 - 로봇 청소기
# Gold 5
# 그래프 이론
#

import sys
input = sys.stdin.readline


def dfs(r, c, d):
    global answer
    if visited[r][c] == False:
        visited[r][c] = True
        answer += 1

    if d == 0:
        if (c-1) in range(M) and not visited[r][c-1] and board[r][c-1] == 0:
            dfs(r, c-1, 3)
        elif (r+1) in range(N) and not visited[r+1][c] and board[r+1][c] == 0:
            dfs(r+1, c, 2)
        elif (c+1) in range(M) and not visited[r][c+1] and board[r][c+1] == 0:
            dfs(r, c+1, 1)
        elif (r-1) in range(N) and not visited[r-1][c] and board[r-1][c] == 0:
            dfs(r-1, c, 0)
        elif (r+1) in range(N) and board[r+1][c] == 0:
            dfs(r+1, c, 0)
        else:
            return False

    if d == 1:
        if (r-1) in range(N) and not visited[r-1][c] and board[r-1][c] == 0:
            dfs(r-1, c, 0)
        elif (c-1) in range(M) and not visited[r][c-1] and board[r][c-1] == 0:
            dfs(r, c-1, 3)
        elif (r+1) in range(N) and not visited[r+1][c] and board[r+1][c] == 0:
            dfs(r+1, c, 2)
        elif (c+1) in range(M) and not visited[r][c+1] and board[r][c+1] == 0:
            dfs(r, c+1, 1)
        elif (c-1) in range(M) and board[r][c-1] == 0:
            dfs(r, c-1, 1)
        else:
            return False

    if d == 2:
        if (c+1) in range(M) and not visited[r][c+1] and board[r][c+1] == 0:
            dfs(r, c+1, 1)
        elif (r-1) in range(N) and not visited[r-1][c] and board[r-1][c] == 0:
            dfs(r-1, c, 0)
        elif (c-1) in range(M) and not visited[r][c-1] and board[r][c-1] == 0:
            dfs(r, c-1, 3)
        elif (r+1) in range(N) and not visited[r+1][c] and board[r+1][c] == 0:
            dfs(r+1, c, 2)
        elif (r-1) in range(N) and board[r-1][c] == 0:
            dfs(r-1, c, 2)
        else:
            return False

    if d == 3:
        if (r+1) in range(N) and not visited[r+1][c] and board[r+1][c] == 0:
            dfs(r+1, c, 2)
        elif (c+1) in range(M) and not visited[r][c+1] and board[r][c+1] == 0:
            dfs(r, c+1, 1)
        elif (r-1) in range(N) and not visited[r-1][c] and board[r-1][c] == 0:
            dfs(r-1, c, 0)
        elif (c-1) in range(M) and not visited[r][c-1] and board[r][c-1] == 0:
            dfs(r, c-1, 3)
        elif (c+1) in range(M) and board[r][c+1] == 0:
            dfs(r, c+1, 3)
        else:
            return False


N, M = map(int, input().split())
r, c, d = map(int, input().split())

answer = 0
board = []
visited = [[False for _ in range(M)] for _ in range(N)]
for _ in range(N):
    board.append(list(map(int, input().split())))
dfs(r, c, d)
print(answer)
