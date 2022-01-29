# 
# Baekjoon 1188 - 음식 평론가
# Gold 5 
# 수학
# 

import sys
import math


def solution():
    (num_of_food, num_of_people) = map(int, sys.stdin.readline().rstrip().split())
    return num_of_people - math.gcd(num_of_food, num_of_people)
  

print(solution())