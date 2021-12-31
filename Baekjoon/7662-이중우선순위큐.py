import sys
from queue import PriorityQueue


def test():
    min_queue = PriorityQueue()
    max_queue = PriorityQueue()
    min_del = PriorityQueue()
    max_del = PriorityQueue()
    k = int(sys.stdin.readline().rstrip())
    q_size = 0
    for i in range(k):
        (oper, value) = sys.stdin.readline().rstrip().split()
        value = int(value)
        if oper == "I":
            min_queue.put(value)
            max_queue.put(-value)
            q_size += 1
            continue
        if q_size == 0:
            continue
        q_size -= 1
        if value == -1:
            min_del.put(-min_queue.get())
        if value == 1:
            max_del.put(-max_queue.get())
    if q_size == 0:
        print("EMPTY")
        return True
    answer = [0, 0]
    while True:
        max_val = max_queue.get()
        if min_del.qsize() == 0:
            answer[0] = -max_val
            break
        min_del_val = min_del.get()
        if max_val != min_del_val:
            answer[0] = -max_val
            break
    while True:
        min_val = min_queue.get()
        if max_del.qsize() == 0:
            answer[1] = min_val
            break
        max_del_val = max_del.get()
        if min_val != max_del_val:
            answer[1] = min_val
            break
    print(answer[0], answer[1])
    return True


def solution():
    t = int(sys.stdin.readline().rstrip())
    for _ in range(t):
        test()
  
  
solution()