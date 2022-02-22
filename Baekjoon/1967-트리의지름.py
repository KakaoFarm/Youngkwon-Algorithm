#
# Baekjoon 1967 - 트리의 지름
# Gold 4
# 그래프 이론, 트리
#

import sys
from collections import deque
input = sys.stdin.readline


def get_max_value_and_index(lst):
    _max = [-1, -float('inf')]
    for i in range(len(lst)):
        if lst[i] > _max[1]:
            _max = [i, lst[i]]
    return _max


def bfs(start_node):
    visited = [-1 for _ in range(N+1)]
    q = deque()
    q.append((0, start_node))
    while q:
        curr_dist, node = q.popleft()
        visited[node] = curr_dist
        for e, w in graph[node]:
            if visited[e] == -1:
                q.append((curr_dist + w, e))
    return visited


N = int(input())
graph = [[] for _ in range(N+1)]

for _ in range(N-1):
    a, b, w = map(int, input().split())
    graph[a].append((b, w))
    graph[b].append((a, w))

_max = get_max_value_and_index(bfs(1))
_max = get_max_value_and_index(bfs(_max[0]))
print(_max[1])
