#
# Baekjoon 1208 - 부분 수열의 합 2
# Gold 1
# 이분 탐색
#

from itertools import combinations
from collections import defaultdict


def get_possible_sum_list(lst):
    dic = defaultdict(int)
    for length in range(1, len(lst)+1):
        cl = list(map(list, combinations(lst, length)))
        for v_lst in cl:
            dic[sum(v_lst)] += 1
    return dic


def main():
    n, s = map(int, input().split())
    lst = sorted(list(map(int, input().split())))
    left, right = lst[:n//2], lst[n//2:]
    left_sum = get_possible_sum_list(left)
    right_sum = get_possible_sum_list(right)

    answer = left_sum[s] + right_sum[s]

    for s1 in left_sum:
        if s-s1 in right_sum:
            answer += left_sum[s1] * right_sum[s-s1]

    print(answer)


main()
