#
# Baekjoon 1780 - 종이의 개수
# Silver 2
# 분할정복, 재귀
#

import sys
input = sys.stdin.readline


def recursion(x, y, size):
    left_top = paper[x][y]

    for i in range(x, x+size):
        for j in range(y, y+size):
            if(paper[i][j] != left_top):
                for k in range(3):
                    for l in range(3):
                        recursion(x + (k*size)//3, y + (l*size)//3, size//3)
                return
    answer[left_top+1] += 1


N = int(input())
paper = [list(map(int, input(). split())) for _ in range(N)]
answer = [0, 0, 0]
recursion(0, 0, N)

print(answer[0])
print(answer[1])
print(answer[2])
