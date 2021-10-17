from collections import deque

def solution(numbers, target):
    answer = 0
    queue = deque() # value, depth
    queue.append((0,0))
    while queue:
        value, depth = queue.popleft()
        if value == target and depth == len(numbers):
            answer += 1
        elif depth >= len(numbers):
            pass
        else:
            queue.append((value + numbers[depth], depth + 1))
            queue.append((value - numbers[depth], depth + 1))
    return answer
