#
# Baekjoon 2533 - 사회망 서비스(SNS)
# Gold 3
# 트리, 다이나믹 프로그래밍
#

import sys
sys.setrecursionlimit(10 ** 9)
input = sys.stdin.readline

N = int(input())
tree = [[] for _ in range(N+1)]
dp = [[0, 0] for _ in range(N+1)]
for _ in range(N-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

visited = [False for _ in range(N+1)]


def dfs(start):
    global tree
    global visited
    visited[start] = True

    if len(tree[start]) == 0:
        dp[start][1] = 1
        dp[start][0] = 0
    else:
        for adj in tree[start]:
            if not visited[adj]:
                dfs(adj)
                dp[start][1] += min(dp[adj][0], dp[adj][1])
                dp[start][0] += dp[adj][1]
        dp[start][1] += 1


dfs(1)
print(min(dp[1][0], dp[1][1]))
