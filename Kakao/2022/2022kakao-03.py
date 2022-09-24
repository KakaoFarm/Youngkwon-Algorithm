from itertools import product
from copy import deepcopy
from heapq import heappush, heappop


def solution(users, emoticons):
    disc = [10, 20, 30, 40]
    rec = []

    l = list(product(disc, repeat=len(emoticons)))
    for m in l:
        e = deepcopy(emoticons)

        for i in range(len(e)):
            e[i] = (m[i], e[i] * ((100 - m[i]) / 100))

        plus, money = 0, 0
        for percent, price in users:
            cost = 0
            for d, c in e:
                if d >= percent:
                    cost += c
            if cost >= price:
                plus += 1
            else:
                money += cost
        heappush(rec, (-plus, -money))

    answer = list(heappop(rec))
    answer[0], answer[1] = -answer[0], int(-answer[1])
    return answer


print(solution([[40, 2900], [23, 10000]], [11, 5200], [
      5, 5900], [40, 3100], [27, 9200], [32, 6900], [7000, 9000]))
print(solution([[40, 2900], [23, 10000], [11, 5200],
      [5, 5900], [40, 3100], [27, 9200], [32, 6900]], [1300, 1500, 1600, 4900]))
