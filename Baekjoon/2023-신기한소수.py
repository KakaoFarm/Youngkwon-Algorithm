# 
# Baekjoon 2023 - 신기한 소수
# Gold 5 
# 수학
# 

import math
import sys

def solution():
    n = int(sys.stdin.readline().rstrip())
    prime = {}
    prime[1] = [2, 3, 5, 7]
    
    for i in range(2, n + 1):
        prime[i] = []
        priv_prime = prime[i - 1]
        for priv_p in priv_prime:
            for offset in range(0, 10):
                num = (priv_p * 10) + offset
                if is_prime_number(num):
                    prime[i].append(num)
    
    for num in prime[n]:
        print(num)
        
                
def is_prime_number(x):
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True
  

solution()