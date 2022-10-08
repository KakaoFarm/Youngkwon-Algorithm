#
# Baekjoon 14267 - 회사 문화1
# Gold 4
# 트리, 그래프 이론
#

import sys
input = sys.stdin.readline


graph = []
point = []


def solution():
    global graph, point
    n, m = map(int, input().split())
    graph = [[] for _ in range(n+1)]
    _index = 2
    for b in list(map(int, input().split()))[1:]:
        graph[b].append(_index)
        _index += 1

    point = [0 for _ in range(n+1)]
    for _ in range(m):
        i, w = map(int, input().split())
        point[i] += w

    for i in range(2, n):
        for adj in graph[i]:
            point[adj] += point[i]


solution()
answer = ""
for p in point[1:]:
    answer += str(p) + " "
print(answer[:-1])
