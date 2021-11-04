# 삼성 SW 역량 테스트
# 조건 1. 비어있는 칸 중에서 좋아하는 학생이 인접한 칸에 가장 많은 칸으로 자리를 정한다.
# 조건 2. 1을 만족하는 칸이 여러 개이면, 인접한 칸 중에서 비어있는 칸이 가장 많은 칸으로 자리를 정한다.
# 조건 3. 2를 만족하는 칸도 여러 개인 경우에는 행의 번호가 가장 작은 칸으로, 그러한 칸도 여러 개이면 열의 번호가 가장 작은 칸으로 자리를 정한다.


import sys

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

N = int(input())
stud = {}
seat = [[0 for e in range(N)] for f in range(N)]
for _ in range(N*N):
    a, b, c, d, e = map(int, sys.stdin.readline().rstrip().split())
    stud[a] = [b, c, d, e]


def solution():
    for key in stud.keys():
        first_cond = get_max_adjoin(key)
        if len(first_cond) == 1:
            i, k = first_cond[0]
            seat[i][k] = key
        else:
            second_cond = get_max_empty(first_cond)
            i, k = second_cond[0]
            seat[i][k] = key
    print(get_satisfaction())


def get_max_adjoin(who):
    result = []
    count_lst = [[-1 for e in range(N)] for f in range(N)]
    max_val = 0
    count = 0
    for i in range(N):
        for k in range(N):
            if seat[i][k] == 0:
                count = 0
                for j in range(4):
                    nx = i + dx[j]
                    ny = k + dy[j]
                    if nx in range(N) and ny in range(N):
                        if seat[nx][ny] in stud[who]:
                            count += 1
                count_lst[i][k] = count
                max_val = max(max_val, count)

    for i in range(N):
        for k in range(N):
            if count_lst[i][k] == max_val:
                result.append((i, k))

    return result


def get_max_empty(tup_lst):
    result = []
    count_lst = [[-1 for e in range(N)] for f in range(N)]
    max_val = 0
    count = 0
    for i, k in tup_lst:
        if seat[i][k] == 0:
            count = 0
            for j in range(4):
                nx = i + dx[j]
                ny = k + dy[j]
                if nx in range(N) and ny in range(N):
                    if seat[nx][ny] == 0:
                        count += 1
            count_lst[i][k] = count
            max_val = max(max_val, count)

    for i in range(N):
        for k in range(N):
            if count_lst[i][k] == max_val:
                result.append((i, k))

    return result


def get_satisfaction():
    result = 0
    count_lst = [[0 for e in range(N)] for f in range(N)]
    count = 0
    for i in range(N):
        for k in range(N):
            count = 0
            for j in range(4):
                nx = i + dx[j]
                ny = k + dy[j]
                if nx in range(N) and ny in range(N):
                    if seat[nx][ny] in stud[seat[i][k]]:
                        count += 1
            count_lst[i][k] = count

    for i in range(N):
        for k in range(N):
            if count_lst[i][k] == 0:
                result += 0
            if count_lst[i][k] == 1:
                result += 1
            if count_lst[i][k] == 2:
                result += 10
            if count_lst[i][k] == 3:
                result += 100
            if count_lst[i][k] == 4:
                result += 1000
    return result


solution()
