# 
# Baekjoon 1339 - 단어 수학
# Gold 4 
# 그리디 알고리즘
# 

import sys


def solution():
    n = int(sys.stdin.readline().rstrip())
    words = []
    dict = {}
    for _ in range(n):
        words.append(sys.stdin.readline().rstrip())
        
    for word in words:
        for i in range(len(word)):
            if word[i] in dict.keys():
                dict[word[i]] += 10 ** (len(word) - (i + 1))
            else:
                dict[word[i]] = 10 ** (len(word) - (i + 1))
    
    value_list = list(sorted(list(dict.values()), reverse=True))
    
    answer = 0
    offset = 9
    for val in value_list:
        answer += (val * offset)
        offset -= 1
        
    print(answer)
    
    
solution()