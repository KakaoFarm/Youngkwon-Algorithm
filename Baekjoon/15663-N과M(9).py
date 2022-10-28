#
# Baekjoon 15663 - N과 M (9)
# Silver 2
# 백트래킹
#
from itertools import permutations


def main():
  n, m = map(int, input().split())
  lst = list(map(int, input().split()))
  ans_lst = list(map(tuple, permutations(lst, m)))
  ans_set = sorted(set(ans_lst))
  ans_set = map(list, ans_set)
  for lst in ans_set:
    print(' '.join(map(str, lst)))
  


main()