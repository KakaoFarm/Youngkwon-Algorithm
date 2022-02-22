#
# Baekjoon 1865 - 웜홀
# Gold 3
# 그래프 이론, 벨만포드
#

import sys
input = sys.stdin.readline


def bf():
    dist = [2200000000 for _ in range(N+1)]
    dist[1] = 0
    for _ in range(N-1):
        for node in graph:
            for e, w in graph[node].items():
                if dist[e] > dist[node] + w:
                    dist[e] = dist[node] + w

    for node in graph:
        for e, w in graph[node].items():
            if dist[e] > dist[node] + w:
                return True
    return False


TC = int(input())
for _ in range(TC):
    graph = {}
    N, M, W = map(int, input().split())
    for __ in range(M):
        S, E, T = map(int, input().split())
        # 도로는 양방향성
        if S not in graph:
            graph[S] = {}
        if E not in graph:
            graph[E] = {}

        if E in graph[S]:
            graph[S][E] = min(graph[S][E], T)
        else:
            graph[S][E] = T
        if S in graph[E]:
            graph[E][S] = min(graph[E][S], T)
        else:
            graph[E][S] = T

    for __ in range(W):
        S, E, T = map(int, input().split())
        if S not in graph:
            graph[S] = {}

        if E in graph[S]:
            # 웜홀은 단방향성
            graph[S][E] = min(graph[S][E], -T)
        else:
            graph[S][E] = -T
    print('YES' if bf() == True else 'NO')
