#
# Baekjoon 1162 - 도로포장
# Gold 1
# 그래프이론, 다익스트라
#
from heapq import heappush, heappop
MAX_DIST = float('inf')


def dijkstra(graph, start, end, pass_cnt):
    q = []
    heappush(q, [0, start, pass_cnt, [MAX_DIST
             for _ in range(len(graph))]])
    while q:
        curr_dist, node, cnt, min_dist = heappop(q)

        if node == end:
            return curr_dist
        for k in graph[node]:
            if curr_dist + graph[node][k] < min_dist[k]:
                temp_dist = min_dist
                temp_dist[k] = curr_dist + graph[node][k]
                heappush(q, [min_dist[k], k, cnt, temp_dist])
            if cnt > 0 and curr_dist < min_dist[k]:
                min_dist[k] = curr_dist
                heappush(q, [curr_dist, k, cnt-1, min_dist])


def main():
    n, m, k = map(int, input().split())
    graph = [{} for _ in range(n+1)]

    for _ in range(m):
        a, b, dist = map(int, input().split())
        if b not in graph[a]:
            graph[a][b] = dist
            graph[b][a] = dist
        else:
            graph[a][b] = min(graph[a][b], dist)
            graph[b][a] = min(graph[b][a], dist)

    answer = dijkstra(graph, 1, n, k)
    print(answer)


main()
