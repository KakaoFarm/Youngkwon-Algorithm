import sys


def solution():
    N = int(input())
    S = []
    for _ in range(N):
        a, b = map(int, sys.stdin.readline().rstrip().split())
        S.append([a, b])
    result = recursion(S, 0, 0)
    print(result)


def recursion(lst, index, curr):

    if(index >= len(lst)):
        return curr

    if(index + lst[index][0] > len(lst)):
        return recursion(lst, index + 1, curr)

    return max(recursion(lst, index + 1, curr), recursion(lst, index + lst[index][0], curr + lst[index][1]))


solution()
