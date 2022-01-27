import sys


def solution():
    dp = [1, 1]
    n = int(sys.stdin.readline().rstrip())
    for i in range(2, n + 1):
        dp.append(dp[i-2] + dp[i-1])
    return dp[n] % 10007


print(solution())