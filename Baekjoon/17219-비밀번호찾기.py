#
# Baekjoon 17219 - 비밀번호 찾기
# Silver 4
# 자료구조
#

import sys
input = sys.stdin.readline


N, M = map(int, input().split())
_dict = {}

for _ in range(N):
    site, passwd = map(str, input().split())
    _dict[site] = passwd

for _ in range(M):
    print(_dict[input().rstrip()])
