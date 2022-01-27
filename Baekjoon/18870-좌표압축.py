import sys


def solution():
    n = int(sys.stdin.readline().rstrip())
    origin_x = list(map(int, sys.stdin.readline().rstrip().split()))
    dup_removed_x = list(dict.fromkeys(origin_x))
    sorted_x = sorted(dup_removed_x)
    dic = {}
    for order in range(len(sorted_x)):
        dic[sorted_x[order]] = order
  
    for x in origin_x:
        print(dic[x], end=' ')
    
    
solution()