import sys
from collections import deque
MAX_INDEX = 100000


def solution():
  (n, k) = map(int, sys.stdin.readline().rstrip().split())
  queue = deque([n])
  visit = [False] * (MAX_INDEX + 1)
  new_elem = []
  time = 0
  
  while True:
    while queue:
      elem = queue.popleft()
      if elem == k:
        return time
      visit[elem] = True
      new_elem += [elem-1, elem+1, elem*2]
    for ne in new_elem:
      if ne <= MAX_INDEX and not visit[ne]:
        queue.append(ne)
    new_elem = []
    time += 1


print(solution())