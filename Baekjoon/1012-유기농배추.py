import sys
sys.setrecursionlimit(10**9)


graph = []
row = 0
col = 0


def main():
    t = int(input())
    for _ in range(t):
        solution()


def solution():
    global graph, row, col
    answer = 0
    # row: n , col: m , 배추 개수: k
    m, n, k = map(int, sys.stdin.readline().rstrip().split())
    graph = [[0]*m for _ in range(n)]
    row = n
    col = m
    for _ in range(k):
        c, r = map(int, sys.stdin.readline().rstrip().split())
        graph[r][c] = 1
    
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1:
                dfs(i, j)
                answer += 1
    print(answer)
      
      
def dfs(i, j):
    if i < 0 or i >= row or j < 0 or j >= col:
        return False
    if graph[i][j] == 1:
        graph[i][j] = 0
        dfs(i - 1, j)
        dfs(i, j - 1)
        dfs(i + 1, j)
        dfs(i, j + 1)
    return True
        
        
main()