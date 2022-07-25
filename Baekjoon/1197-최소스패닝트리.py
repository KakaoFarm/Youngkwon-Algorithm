#
# Baekjoon 1197 - 최소 스패닝 트리
# Gold 4
# 그래프 이론, 크루스칼 알고리즘
#

import sys
input = sys.stdin.readline


def get_parent(node):
    while True:
        if parent[node] == node:
            return node
        node = parent[node]


def union_parent(a, b):
    parent_a = get_parent(a)
    parent_b = get_parent(b)
    if parent_a < parent_b:
        parent[parent_b] = parent_a
    else:
        parent[parent_a] = parent_b


V, E = map(int, input().split())
parent = {}
for i in range(1, V + 1):
    parent[i] = i

graph = []
for _ in range(E):
    a, b, c = map(int, input().split())
    graph.append((c, a, b))

graph.sort()

answer = 0
for i in range(E):
    edge, a, b = graph[i]
    if get_parent(a) != get_parent(b):
        union_parent(a, b)
        answer += edge

print(answer)
