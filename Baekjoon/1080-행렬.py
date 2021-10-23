import sys

def toggle(matrix, n, m):
    for i in range(n, n+3):
        for k in range(m, m+3):
            if matrix[i][k] == '0':
                matrix[i][k] = '1'
            else:
                matrix[i][k] = '0'
    return matrix

def solution():
    N, M = map(int, sys.stdin.readline().rstrip().split())
    a = []; b = []; count = 0
    for i in range(N):
        a.append(list(sys.stdin.readline().rstrip()))
    for i in range(N):
        b.append(list(sys.stdin.readline().rstrip()))
    
    for i in range(0, N-2):
        for k in range(0, M-2):
            if a[i][k] != b[i][k]:
                a = toggle(a, i, k)
                count += 1
    if a != b:
        count = -1
    print(count)
    
solution()