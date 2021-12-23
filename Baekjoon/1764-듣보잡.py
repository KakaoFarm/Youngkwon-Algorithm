import sys


def solution():
    (n, m) = list(map(int, sys.stdin.readline().rstrip().split()))
    lst = []
    answer = []
    for i in range(n+m):
        lst.append(sys.stdin.readline().rstrip())
    lst.sort()
    for i in range(n+m-1):
        if lst[i] == lst[i+1]:
            answer.append(lst[i])
            i += 2
    print(len(answer))
    for name in answer:
        print(name)
        

solution()