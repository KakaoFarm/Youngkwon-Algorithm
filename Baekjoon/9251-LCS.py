#
# Baekjoon 9251 - LCS
# Gold 5
# 다이나믹 프로그래밍
#

import sys
input = sys.stdin.readline

S1 = input().rstrip().upper()
S2 = input().rstrip().upper()
len1 = len(S1)
len2 = len(S2)

matrix = [[0 for _ in range(len2+1)] for _ in range(len1+1)]

for i in range(1, len1 + 1):
    for j in range(1, len2 + 1):
        if S1[i-1] == S2[j-1]:
            matrix[i][j] = matrix[i-1][j-1] + 1
        else:
            matrix[i][j] = max(matrix[i-1][j], matrix[i][j-1])

print(matrix[len1][len2])
