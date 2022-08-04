#
# Baekjoon 4386 - 별자리 만들기
# Gold 4
# 그래프 이론, 최소 스패닝 트리
#

from math import sqrt
import sys
input = sys.stdin.readline


def get_parent(i):
    while True:
        if parent[i] == i:
            return i
        i = parent[i]


def union_parent(i, j):
    parent_i = get_parent(i)
    parent_j = get_parent(j)

    if parent_i < parent_j:
        parent[parent_j] = parent_i
    else:
        parent[parent_i] = parent_j


n = int(input())
stars = []
parent = [i for i in range(n)]

for i in range(n):
    x, y = map(float, input().split())
    stars.append((x, y, i))

graph = []
for i in range(n - 1):
    for j in range(i + 1, n):
        graph.append((sqrt((stars[i][0] - stars[j][0]) ** 2 + (
            stars[i][1] - stars[j][1]) ** 2), stars[i][2], stars[j][2]))
graph.sort()

answer = 0
for (dist, start, end) in graph:
    if get_parent(start) != get_parent(end):
        union_parent(start, end)
        answer += dist
print(round(answer, 2))
