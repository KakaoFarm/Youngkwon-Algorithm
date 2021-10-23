import sys

n = int(input())

def solution(n):
  for _ in range(n):
    N, M = map(int, sys.stdin.readline().rstrip().split())
    print(nCk(M, N))
    
def nCk(n, k):
  upper = 1; below = 1
  for i in range(n-(k-1), n+1):
    upper *= i
  for i in range(1, k+1):
    below *= i
  return int(upper / below)

solution(n)