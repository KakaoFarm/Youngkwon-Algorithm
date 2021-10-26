def solution(places):
    answer = [0 for _ in range(len(places))]
    for i in range(len(places)):
        if(is_observing(places[i])):
            answer[i] = 1
    return answer


def is_observing(place):
    for i in range(5):
        for k in range(5):
            if place[i][k] == 'P' and not is_distancing(i, k, place):
                return False
    return True


def is_distancing(i, k, place):
    # Manhattan distance == 1
    for off in [-1, 1]:
        if (arrange(i + off) != i and place[arrange(i + off)][k] == 'P') or (arrange(k + off) != k and place[i][arrange(k + off)] == 'P'):
            return False
    # Manhattan distance == 2
    # 상 하 좌 우
    for scope, between in [(-2, -1), (2, 1)]:
        if place[arrange(i + scope)][k] == 'P' and place[arrange(i + between)][k] != 'X':
            if i != arrange(i + scope):
                return False

        if place[i][arrange(k + scope)] == 'P' and place[i][arrange(k + between)] != 'X':
            if k != arrange(k + scope):
                return False
    # 대각
    for off_i, off_k in [(-1, -1), (-1, 1), (1, -1), (1, 1)]:
        new_i = i + off_i
        new_k = k + off_k
        if (arrange(new_i), arrange(new_k)) == (new_i, new_k):
            if place[new_i][new_k] == 'P' and (place[new_i][k] != 'X' or place[i][new_k] != 'X'):
                return False
    return True


def arrange(num):
    if num < 0:
        return 0
    elif num > 4:
        return 4
    return num
