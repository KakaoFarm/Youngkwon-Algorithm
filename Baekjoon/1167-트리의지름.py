#
# Baekjoon 1167 - 트리의 지름
# Gold 3
# 그래프 이론, 트리
#

import sys
from collections import deque
input = sys.stdin.readline


def get_max_by_bfs(node):
    visited = [-1] * (V+1)
    _max = [0, node]

    q = deque()
    q.append(node)
    visited[node] = 0

    while q:
        n = q.popleft()
        for e, w in graph[n]:
            if visited[e] == -1:
                visited[e] = visited[n] + w
                q.append(e)
                if _max[0] < visited[e]:
                    _max = [visited[e], e]
    return _max


V = int(input())
graph = [[] for _ in range(V+1)]
for _ in range(V):
    line_list = list(map(int, input().split()))[:-1]
    for i in range(1, len(line_list), 2):
        graph[line_list[0]].append((line_list[i], line_list[i+1]))


dis, node = get_max_by_bfs(1)
dis, node = get_max_by_bfs(node)
print(dis)
