import sys


def solution():
    n = int(sys.stdin.readline().rstrip())
    dp = [1] * n
    for i in range(2, n):
        dp[i] = dp[i-2] + dp[i-1]
    print(dp[n-1])


solution()
