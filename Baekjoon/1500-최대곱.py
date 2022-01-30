# 
# Baekjoon 1500 - 최대 곱
# Silver 1
# 수학
# 

import sys

(S, K) = map(int, sys.stdin.readline().rstrip().split())
arr = []

for _ in range(K):
    arr.append(S // K)
    
remain = S - ((S // K) * K)

for i in range(remain):
    arr[i] += 1

answer = 1
for num in arr:
    answer *= num
    
print(answer)