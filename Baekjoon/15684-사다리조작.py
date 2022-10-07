#
# Baekjoon 15684 - 사다리 조작
# Gold 3
# 백트래킹
#

import sys
from itertools import combinations
input = sys.stdin.readline


def check(m):
    for col in range(1, N+1):
        c = col
        for row in range(1, H+1):
            if m[row][c]:
                c += 1
            elif c-1 in range(1, N+1) and m[row][c-1] == True:
                c -= 1
        if c != col:
            return False
    return True


N, M, H = map(int, input().split())
move = [[False for _ in range(N+1)] for _ in range(H+1)]

for _ in range(M):
    a, b = map(int, input().split())
    move[a][b] = True

choice = []
for i in range(1, H+1):
    for j in range(1, N):
        if not move[i][j] and (j+1 not in range(1, N+1) or not move[i][j+1]) and (j-1 not in range(1, N+1) or not move[i][j-1]):
            choice.append((i, j))

answered = False
if check(move):
    print(0)
    answered = True

if not answered:
    for k in range(1, 4):
        sample = list(map(list, combinations(choice, k)))
        for index in range(len(sample)):
            cont_flag = False
            if index - 1 >= 0:
                for i, j in sample[index-1]:
                    move[i][j] = False
            for i, j in sample[index]:
                if move[i][j-1] or move[i][j+1]:
                    cont_flag = True
                    break
                move[i][j] = True
            if cont_flag:
                continue
            if check(move):
                print(k)
                answered = True
                break
        if answered:
            break

if not answered:
    print(-1)
