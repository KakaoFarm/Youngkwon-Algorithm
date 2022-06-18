#
# Baekjoon 15686 - 치킨 배달
# Gold 5
# 구현, 브루트 포스, 백트래킹
#

import sys
from itertools import combinations
input = sys.stdin.readline


def get_dist(start, end):
    sx, sy = start
    ex, ey = end
    return abs(ex - sx) + abs(ey - sy)


N, M = map(int, input().split())
home = []
market = []

for i in range(N):
    _row = list(map(int, input().split()))
    for j in range(N):
        if _row[j] == 1:
            home.append([i, j])
        elif _row[j] == 2:
            market.append([i, j])


dist = [0 for _ in range(len(list(combinations(market, M))))]
for h in home:
    _market = list(combinations(market, M))
    for i in range(len(_market)):
        _min = float('inf')
        for m in _market[i]:
            _min = min(_min, get_dist(h, m))
        dist[i] += _min

print(min(dist))
