import sys


def solution():
    (n, r, c) = list(map(int, sys.stdin.readline().rstrip().split()))
    answer = int(recursion(n, r, c))
    print(answer)



def recursion(n, r, c):
    if r == 0 and c == 0:
        return 0
    mass = 2**(2*n) / 4   # a quarter of 2^2n
    mass_count = 0
    half = (2**n / 2) - 1
    if r > half:
        mass_count += 2
        r -= (half + 1)
    if c > half:
        mass_count += 1
        c -= (half + 1)
    return (mass * mass_count) + recursion(n-1, r, c)
    
    
solution()