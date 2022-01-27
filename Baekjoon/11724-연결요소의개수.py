import sys
sys.setrecursionlimit(10**6)


def solution():
    (N, M) = map(int, sys.stdin.readline().rstrip().split())
    visit = [False] * N
    graph = [[False for __ in range(N)] for _ in range(N)]
    for _ in range(M):
        (u, v) = map(int, sys.stdin.readline().rstrip().split())
        graph[u - 1][v - 1] = True
        graph[v - 1][u - 1] = True
    
    result = 0
    for i in range(N):
        if dfs(i, graph, visit) == True:
            result += 1
            
    return result
                

def dfs(node, graph, visit):
    if visit[node] == True:
        return False
    visit[node] = True
    for j in range(len(graph[node])):
        if graph[node][j] == True:
            dfs(j, graph, visit)
    return True
            
            
print(solution())