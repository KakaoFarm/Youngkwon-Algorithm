#
# Baekjoon 9935 - 문자열 폭발
# Gold 4
# 자료구조, 스택
#

import sys
input = sys.stdin.readline

_str = input().rstrip()
_t = input().rstrip()
_t_last = _t[-1]
_stack = []

for i in range(len(_str)):
    _char = _str[i]
    _stack.append(_char)
    if _char == _t_last:
        if ''.join(_stack[-len(_t):]) == _t:
            del(_stack[-len(_t):])

if len(_stack) == 0:
    _stack = "FRULA"
print(''.join(_stack))
