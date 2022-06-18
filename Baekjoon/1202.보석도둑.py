#
# Baekjoon 1202 - 보석 도둑
# Gold 2
# 그리디 알고리즘, 우선순위 큐
#

import sys
import heapq
input = sys.stdin.readline

N, K = map(int, input().split())

gem = []
for _ in range(N):
    m, v = map(int, input().split())
    heapq.heappush(gem, [m, v])

bag = []
for i in range(K):
    heapq.heappush(bag, int(input()))

ans = 0
capable = []

for _ in range(K):
    _max = heapq.heappop(bag)

    while gem and _max >= gem[0][0]:
        w, v = heapq.heappop(gem)
        heapq.heappush(capable, -v)

    if capable:
        ans -= heapq.heappop(capable)
    elif not gem:
        break

print(ans)
