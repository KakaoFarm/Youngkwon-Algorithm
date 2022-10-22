#
# Baekjoon 9252 - LCS2
# Gold 4
# 다이나믹 프로그래밍
#


def main():
    word1 = list(input())
    word2 = list(input())
    l1, l2 = len(word1), len(word2)
    dp = [['' for _ in range(l2+1)] for _ in range(l1+1)]

    for i in range(1, l1+1):
        for j in range(1, l2+1):
            if word1[i-1] == word2[j-1]:
                dp[i][j] = dp[i-1][j-1] + word1[i-1]
            else:
                if len(dp[i-1][j]) > len(dp[i][j-1]):
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = dp[i][j-1]
    print(len(dp[-1][-1]))
    print(dp[-1][-1])


main()
