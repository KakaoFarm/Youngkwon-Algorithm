import sys
from queue import deque


def solution():
    n = int(sys.stdin.readline().rstrip())
    time_table = []
    for _ in range(n):
        time_table.append(list(map(int, sys.stdin.readline().rstrip().split())))
    queue = deque(sorted(time_table, key=lambda x: (x[1], x[0])))
    cnt = 0
    curr = 0
    while queue:
        [start, end] = queue.popleft()
        if start >= curr:
          curr = end
          cnt += 1
    return cnt
    

print(solution())