#
# Baekjoon 1647 - 도시 분할 계획
# Gold 4
# 그래프 이론, 최소 스패닝 트리
#

import sys
input = sys.stdin.readline


def get_parent(node):
    while True:
        if parent[node] == node:
            return node
        else:
            node = parent[node]


def union_parent(node_a, node_b):
    parent_a = get_parent(node_a)
    parent_b = get_parent(node_b)

    if parent_a < parent_b:
        parent[parent_b] = parent_a
    else:
        parent[parent_a] = parent_b


N, M = map(int, input().split())
parent = {}

for i in range(1, N + 1):
    parent[i] = i

graph = []
for _ in range(M):
    A, B, C = map(int, input().split())
    graph.append((C, A, B))

graph.sort()

answer = []
for i in range(len(graph)):
    (c, a, b) = graph[i]
    if get_parent(a) != get_parent(b):
        union_parent(a, b)
        answer.append(c)

answer.sort()
print(sum(answer[:-1]))
