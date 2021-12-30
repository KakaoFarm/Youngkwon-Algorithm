import sys
from queue import PriorityQueue


def queue_swap(queue):
    new_queue = PriorityQueue()
    for _ in range(queue.qsize()):
        new_queue.put(-queue.get())
    return new_queue


def test():
    queue = PriorityQueue()
    k = int(sys.stdin.readline().rstrip())
    is_min_queue = True
    for i in range(k):
        (oper, value) = sys.stdin.readline().rstrip().split()
        value = int(value)
        if oper == "I":
            if not is_min_queue:
                queue = queue_swap(queue)
                is_min_queue = not is_min_queue
            queue.put(value)
            continue
        if queue.qsize() == 0:
            continue
        if (value == -1 and not is_min_queue) or (value == 1 and is_min_queue):
            queue = queue_swap(queue)
            is_min_queue = not is_min_queue
        queue.get()
    if queue.qsize() == 0:
        print("EMPTY")
    elif queue.qsize() == 1:
        value = queue.get()
        print(value, value)
    else:
        answer = [0, 0]
        index = [0, 1]
        if is_min_queue:
            index = [1, 0]
        for i in index:
            answer[i] = queue.get()
            queue = queue_swap(queue)
        print(-answer[0], answer[1])


def solution():
    t = int(sys.stdin.readline().rstrip())
    for _ in range(t):
        test()
  
  
solution()