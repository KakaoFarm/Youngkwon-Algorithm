#
# Baekjoon 1613 - 역사
# Gold 3
# 그래프 이론, 플로이드–와샬
#

import sys
input = sys.stdin.readline


(N, K) = map(int, input().split())
graph = [[0 for _ in range(N+1)] for _ in range(N+1)]

for _ in range(K):
    (a, b) = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = -1

# 플로이드-와샬
# Index 접근 순서 중요!
for k in range(N+1):
    for i in range(N+1):
        for j in range(N+1):
            if graph[i][j] == 0:
                if graph[i][k] == 1 and graph[k][j] == 1:
                    graph[i][j] = 1
                elif graph[i][k] == -1 and graph[k][j] == -1:
                    graph[i][j] = -1

T = int(input())
for _ in range(T):
    (ta, tb) = map(int, input().split())
    print(-graph[ta][tb])
