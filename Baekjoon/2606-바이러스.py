import sys
from queue import deque


def solution():
    comp = int(sys.stdin.readline().rstrip())
    network = int(sys.stdin.readline().rstrip())
    graph = [[] for _ in range(comp)]
    visit = [False] * comp
    positive = 0
    for _ in range(network):
        (n1, n2) = map(int, sys.stdin.readline().rstrip().split())
        graph[n1-1].append(n2-1)
        graph[n2-1].append(n1-1)
    queue = deque([0])
    while queue:
        com = queue.popleft()
        visit[com] = True
        positive += 1
        for node in graph[com]:
            if not visit[node] and node not in queue:
                queue.append(node)
    return positive - 1 # Except the origin


print(solution())