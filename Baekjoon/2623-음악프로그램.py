#
# Baekjoon 2623 - 음악프로그램
# Gold 3
# 그래프 이론, 위상정렬
#

from queue import deque


def main():
    n, m = map(int, input().split())
    aft_graph = [[] for _ in range(n+1)]
    pre_num = [0 for _ in range(n+1)]
    q = []
    answer = []

    for _ in range(m):
        lst = list(map(int, input().split()))
        num, order_list = lst[0], lst[1:]

        for i in range(num-1, -1, -1):
            for j in range(i-1, -1, -1):
                if order_list[i] not in aft_graph[order_list[j]]:
                    aft_graph[order_list[j]].append(order_list[i])
                    pre_num[order_list[i]] += 1

    for idx in range(1, n+1):
        if pre_num[idx] == 0:
            q.append(idx)

    q = deque(q)
    while q:
        person = q.popleft()
        answer.append(person)
        for adj in aft_graph[person]:
            pre_num[adj] -= 1
            if pre_num[adj] == 0:
                q.append(adj)

    if len(answer) != n:
        print(0)
    else:
        for person in answer:
            print(person)


main()
