import sys


def solution():
    t = int(sys.stdin.readline().rstrip())
    dp = [None]*10
    dp[0] = 1
    dp[1] = 2
    dp[2] = 4
    for i in range(t):
        n = int(sys.stdin.readline().rstrip())
        for j in range(3, n):
            if dp[j] == None:
                dp[j] = dp[j-3] + dp[j-2] + dp[j-1]
        print(dp[n-1])


solution()
