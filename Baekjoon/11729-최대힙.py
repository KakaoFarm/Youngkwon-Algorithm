import sys
from queue import PriorityQueue


def solution():
    q = PriorityQueue()
    n = int(sys.stdin.readline().rstrip())
    for _ in range(n):
        x = int(sys.stdin.readline().rstrip())
        if(x != 0):
            q.put(-x)
        else:
            if(q.qsize() == 0):
                print(0)
            else:
                print(-(q.get()))
                

solution()