#
# Baekjoon 14725 - 개미굴
# Gold 3
# 트리
#

def dfs(graph, level):
    for k in sorted(graph.keys()):
        print('--'*level + k)
        dfs(graph[k], level+1)


def main():
    n = int(input())
    graph = {}

    for _ in range(n):
        lst = input().split()
        num, lst = lst[0], lst[1:]
        g = graph
        for node in lst:
            if node not in g.keys():
                g[node] = {}
                g = g[node]
            else:
                g = g[node]

    dfs(graph, 0)


main()
