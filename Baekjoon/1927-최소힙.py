import sys
from queue import PriorityQueue


def solution():
    queue = PriorityQueue()
    n = int(sys.stdin.readline().rstrip())
    for _ in range(n):
        x = int(sys.stdin.readline().rstrip())
        if x == 0:
            if queue.qsize() == 0:
              print(0)
            else:
              print(queue.get())
        else:
            queue.put(x)
          

solution()
