#
# Baekjoon 2887 - 행성 터널
# Platinum 5
# 그래프 이론, 최소 스패닝 트리
#

import sys
input = sys.stdin.readline


def get_dist(node1, node2):
    x1, y1, z1, n1 = node1
    x2, y2, z2, n2 = node2
    return min(abs(x1 - x2), abs(y1 - y2), abs(z1 - z2))


def get_parent(node):
    while True:
        if parent[node] == node:
            return node
        else:
            node = parent[node]


def union_node(node1, node2):
    parent1 = get_parent(node1)
    parent2 = get_parent(node2)

    if parent1 < parent2:
        parent[parent2] = parent[parent1]
    else:
        parent[parent1] = parent[parent2]


N = int(input())
node = []
parent = {}
for i in range(N):
    x, y, z = map(int, input().split())
    node.append((x, y, z, i))
    parent[i] = i

graph = []
for i in range(3):
    node.sort(key=lambda x: x[i])
    for j in range(N - 1):
        graph.append((get_dist(node[j], node[j+1]),
                     node[j][3], node[j + 1][3]))
graph.sort()

answer = 0
for i in range(len(graph)):
    dist, a, b = graph[i]
    if get_parent(a) != get_parent(b):
        union_node(a, b)
        answer += dist
print(answer)
