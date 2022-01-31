# 
# Baekjoon 2212 - 센서
# Gold 5
# 그리디 알고리즘
# 

import sys

N = int(sys.stdin.readline().rstrip())
K = int(sys.stdin.readline().rstrip())
sensors = list(map(int, sys.stdin.readline().rstrip().split()))
sensors = sorted(sensors)
gaps = []

for i in range(len(sensors) - 1):
    gap = sensors[i+1] - sensors[i]
    gaps.append(gap)
    
gaps = sorted(gaps, reverse=True)
gaps = gaps[K-1:]

answer = 0
for gap in gaps:
    answer += gap

print(answer)