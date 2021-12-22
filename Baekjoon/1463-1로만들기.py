import sys

def solution():
    dp = [None] * (10**6)
    dp[0] = 0
    dp[1] = 1
    dp[2] = 1
    dp[3] = 2
    
    n = int(sys.stdin.readline().rstrip())
    for i in range(4, n):
        check_flag = True
        count = 0
        temp = i
        while check_flag:
            if temp % 3 == 0:
                temp = temp // 3
                count += 1
                if dp[temp] != None:
                    dp[i] = dp[temp] + count
                    check_flag = False
            else:
              break
        while check_flag:
            if temp % 2 == 0:
                temp = temp // 2
                count += 1
                if dp[temp] != None:
                    dp[i] = dp[temp] + count
                    check_flag = False
            else:
              break