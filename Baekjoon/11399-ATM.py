import sys
from queue import PriorityQueue

def solution():
    answer = 0
    time = 0
    n = sys.stdin.readline().rstrip()
    p = sys.stdin.readline().rstrip().split()
    time_queue = PriorityQueue()
    for t in p:
        time_queue.put(int(t))
        
    while(time_queue.qsize() != 0):
        time += time_queue.get()
        answer += time
        
    return answer
  
print(solution())