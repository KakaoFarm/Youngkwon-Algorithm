from math import floor
import sys

count = 1
N, a, b = map(int, sys.stdin.readline().rstrip().split())

def is_matched(a, b):
    a += 1; b += 1
    return floor(a / 2) == floor(b / 2)

def reassign(n):
    if n % 2 == 1:
        n += 1
    return n / 2

while(True):
    if is_matched(a, b):
        print(count)
        break
    (a, b) = (reassign(a), reassign(b))
    count += 1