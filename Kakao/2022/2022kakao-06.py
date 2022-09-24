from queue import deque
from heapq import heappush, heappop

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def solution(n, m, x, y, r, c, k):

    left_count = 0
    right_count = 0
    up_count = 0
    down_count = 0
    if x - r > 0:
        up_count += (x-r)
    elif x - r < 0:
        down_count += (r-x)
    if y - c < 0:
        right_count += (c-y)
    elif y - c > 0:
        left_count += (y-c)

    all_count = left_count + right_count + up_count + down_count
    if k > all_count:
        remain = k - all_count
        if remain % 2 == 0:
            move_count = remain // 2
            if down_count > 0:
                temp = move_count
                while True:
                    if r + temp > n:
                        temp -= 1
                    else:
                        break
                down_count += temp
                up_count += temp
                move_count -= temp
            elif up_count > 0:
                temp = move_count
                while True:
                    if x + temp > n:
                        temp -= 1
                    else:
                        break
                down_count += temp
                up_count += temp
                move_count -= temp

            if move_count > 0 and left_count > 0:
                temp = move_count
                while True:
                    if c - temp < 1:
                        temp -= 1
                    else:
                        break
                left_count += temp
                right_count += temp
                move_count -= temp
            elif move_count > 0 and right_count > 0:
                temp = move_count
                while True:
                    if y - temp < 1:
                        temp -= 1
                    else:
                        break
                left_count += temp
                right_count += temp
                move_count -= temp

            path = ("d" * down_count) + ("l" * left_count) + \
                ("r" * right_count) + ("u" * up_count)
            # 청산 안됐을 경우 rl 체크
            if move_count > 0:
                if left_count > 0:
                    path += "r" * move_count + "l" * move_count
                    move_count -= 1

            return path
        else:
            return 'impossible'
    elif k == all_count:
        return ("d" * down_count) + ("l" * left_count) + ("r" * right_count) + ("u" * up_count)
    else:
        return 'impossible'


print(solution(
    3, 4, 2, 3, 3, 1, 5))
