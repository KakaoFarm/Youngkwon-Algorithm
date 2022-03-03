#
# Baekjoon 1541 - 잃어버린 괄호
# Silver 2
# 그리디 알고리즘
#

import sys
input = sys.stdin.readline

_str = input() + 'E'
parsed_list = ['+']
temp = ""
plus_flag = False
plus_flag_lst = []
for i in range(0, len(_str)):
    char = _str[i]
    if (char == '+' and not plus_flag):
        parsed_list.append(int(temp))
        parsed_list.append('+')
        temp = ""
    elif (char == '+' and plus_flag):
        plus_flag_lst.append(int(temp))
        temp = ""
    elif (char == '-'):
        plus_flag = not plus_flag
        # plus_flag가 열림
        if (plus_flag):
            parsed_list.append(int(temp))
        # plus_flag가 닫힘
        if(not plus_flag):
            parsed_list.append(sum(plus_flag_lst) + int(temp))
            plus_flag_lst = []
            plus_flag = True
        parsed_list.append('-')
        temp = ""
    elif (char != 'E'):
        temp += char
    elif (char == 'E'):
        if (plus_flag):
            parsed_list.append(sum(plus_flag_lst) + int(temp))
        else:
            parsed_list.append(int(temp))

answer = 0
for i in range(1, len(parsed_list), 2):
    # 숫자만 for loop
    st = parsed_list[i]
    if parsed_list[i-1] == '+':
        answer += st
    else:
        answer -= st
print(answer)
