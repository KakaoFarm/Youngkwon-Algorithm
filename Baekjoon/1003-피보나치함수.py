import sys

dp = [None] * 41
dp[0] = (1,0)
dp[1] = (0,1)
dp[2] = (1,1)
dp[3] = (1,2)


def solution():
    t = int(sys.stdin.readline().rstrip())
    for _ in range(t):
        n = int(sys.stdin.readline().rstrip())
        fibonacci(n)
        print(dp[n][0], dp[n][1])
        
        
def fibonacci(n):
    for i in range(4, n+1):
        if dp[i] == None:
          dp[i] = (dp[i-2][0] + dp[i-1][0], dp[i-2][1] + dp[i-1][1])


solution()