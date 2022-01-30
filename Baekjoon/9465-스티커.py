# 
# Baekjoon 9465 - 스티커
# Silver 1
# 다이나믹 프로그래밍
# 

import sys

# 테스트 케이스 횟수
T = int(sys.stdin.readline().rstrip())

for _ in range(T):
    sticker = []
    n = int(sys.stdin.readline().rstrip())
        
    for _ in range(2):
        sticker.append(list(map(int, sys.stdin.readline().rstrip().split())))

    if n == 1:
        print(max(sticker[0][0], sticker[1][0]))
    
    else:
        dp = [[0 for _ in range(n)] for _ in range(2)]
        dp[0][0] = sticker[0][0]
        dp[1][0] = sticker[1][0]
        dp[0][1] = dp[1][0] + sticker[0][1]
        dp[1][1] = dp[0][0] + sticker[1][1]

        for i in range(2, n):
            for j in range(2):
                dp[j][i] = max(dp[int(not j)][i-2], dp[int(not j)][i-1]) + sticker[j][i]
        
        print(max(dp[0][-1], dp[1][-1]))