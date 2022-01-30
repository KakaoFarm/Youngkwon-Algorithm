# 
# Baekjoon 1263 - 시간 관리
# Silver 1
# 그리디 알고리즘, 정렬
# 

import sys

N = int(sys.stdin.readline().rstrip())
task = []

for _ in range(N):
    time_and_dead_arr = list(map(int, sys.stdin.readline().rstrip().split()))
    task.append(time_and_dead_arr)

task = sorted(task, key=lambda x: x[1], reverse=True)

curr_dead = 10 ** 6
for i in range(len(task)):
    (time, dead) = task[i]
    if dead < curr_dead:
        curr_dead = dead
    
    curr_dead -= time
    if curr_dead < 0:
        curr_dead = -1
        break

print(curr_dead)