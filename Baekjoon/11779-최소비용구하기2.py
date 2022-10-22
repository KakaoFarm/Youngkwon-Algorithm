#
# Baekjoon 11779 - 최소비용 구하기 2
# Gold 3
# 그래프이론, 다익스트라
#
from heapq import heappush, heappop


def main():
    n = int(input())
    m = int(input())
    graph = [[100000 for _ in range(n+1)] for _ in range(n+1)]
    for _ in range(m):
        start, end, cost = map(int, input().split())
        graph[start][end] = min(cost, graph[start][end])

    _start, _end = map(int, input().split())
    dist = [float('inf') for _ in range(n+1)]
    path = [[] for _ in range(n+1)]
    dist[_start] = 0
    path[_start] = [_start]
    q = []
    heappush(q, (0, _start, [_start]))  # d, node, p
    while q:
        d, node, p = heappop(q)
        for i in range(1, n+1):
            if graph[node][i] == 100000:
                continue
            if d + graph[node][i] < dist[i]:
                dist[i] = d + graph[node][i]
                path[i] = p + [i]
                heappush(q, (dist[i], i, path[i]))
    print(dist[_end])
    print(len(path[_end]))
    print(' '.join(map(str, path[_end])))


main()
