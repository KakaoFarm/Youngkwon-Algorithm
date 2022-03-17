#
# Baekjoon 9466 - 텀 프로젝트
# Gold 3
# 그래프 이론
#

import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline


def dfs(node):
    global stack, result
    visited[node] = True
    stack.append(node)
    adj = graph[node]

    if visited[adj]:
        if adj in stack:
            result += stack[stack.index(adj):]
        return
    else:
        dfs(adj)


T = int(input())
for _ in range(T):
    N = int(input())
    graph = [0]
    visited = [False] * (N + 1)
    stack = []
    result = []
    graph += list(map(int, input().split()))

    for i in range(1, N + 1):
        if not visited[i]:
            stack = []
            dfs(i)

    print(N - len(result))
