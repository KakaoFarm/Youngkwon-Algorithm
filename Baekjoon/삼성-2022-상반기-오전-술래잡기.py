#
# 삼성 SW 역량 평가 - 2022 상반기 오전 - 술래 잡기
# 구현, 시뮬레이션
#

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


# 달팽이 모양으로 이동하는 순서에 맞게 index_list 획득
def get_order_list(n):
    x, y, d = n//2, n//2, 3
    order_list = []
    visited = [[False for _ in range(n)] for _ in range(n)]
    visited[x][y] = True

    while True:  # 나가는 방향
        x = x + dx[d]
        y = y + dy[d]
        visited[x][y] = True

        if d == 3 and not visited[x][y+1]:
            d = 0
        elif d == 0 and not visited[x+1][y]:
            d = 1
        elif d == 1 and not visited[x][y-1]:
            d = 2
        elif d == 2 and not visited[x-1][y]:
            d = 3

        if (x, y) == (0, 0):
            d = 1
            order_list.append([x, y, d])
            break

        order_list.append([x, y, d])

    visited = [[False for _ in range(n)] for _ in range(n)]
    visited[x][y] = True
    while True:  # 돌아오는 방향
        x = x + dx[d]
        y = y + dy[d]
        visited[x][y] = True

        nx = x + dx[d]
        ny = y + dy[d]

        # 영역을 벗어나거나 막혀있으면 방향 돌리기
        if (nx not in range(n) or ny not in range(n)) or (visited[nx][ny]):
            if d == 3:
                d = 2
            elif d == 0:
                d = 3
            elif d == 1:
                d = 0
            elif d == 2:
                d = 1

        if (x, y) == (n//2, n//2):
            d = 3
            order_list.append([x, y, d])
            break
        order_list.append([x, y, d])
    return order_list


# 도망자 움직임
def runner_move(runners, board, cx, cy):
    limit = range(len(board))
    new_runners = []
    for i in range(len(runners)):
        if runners[i] == False:
            new_runners.append(False)
            continue

        x, y, d = runners[i]
        if abs(x - cx) + abs(y - cy) > 3:  # 거리가 3 이상인 경우, 기존 위치 유지
            new_runners.append([x, y, d])
            continue

        nx = x + dx[d]
        ny = y + dy[d]
        if nx not in limit or ny not in limit:
            d = (d + 2) % 4
        new_x = x + dx[d]
        new_y = y + dy[d]

        if (new_x, new_y) == (cx, cy):  # 술래가 있으면
            new_runners.append([x, y, d])  # 이전 위치 그대로 추가
        elif board[new_x][new_y] == 'T':  # 나무가 있으면
            if board[x][y] == 'T':
                pass
            elif len(board[x][y]) == 1:
                board[x][y] = 10
            else:
                new_list = []
                for runner in board[x][y]:
                    if runner != -i:
                        new_list.append(runner)
                board[x][y] = new_list

            new_runners.append([new_x, new_y, d])  # board는 수정 안함
        elif board[new_x][new_y] == 10:  # 빈 공간이면
            if board[x][y] != 'T':
                new_list = []
                for runner in board[x][y]:
                    if runner != -i:
                        new_list.append(runner)
                board[x][y] = new_list
            board[new_x][new_y] = [-i]
            new_runners.append([new_x, new_y, d])
        else:
            if board[x][y] != 'T':
                new_list = []
                for runner in board[x][y]:
                    if runner != -i:
                        new_list.append(runner)
                board[x][y] = new_list
            board[new_x][new_y].append(-i)
            new_runners.append([new_x, new_y, d])

    return new_runners, board


# 도망자 잡기
def scan(x, y, d, board, runners):
    limit = range(len(board))
    count = 0
    for dist in range(3):
        nx = x + (dx[d] * dist)
        ny = y + (dy[d] * dist)
        if nx not in limit or ny not in limit:
            break
        if board[nx][ny] != 10 and board[nx][ny] != 'T':
            for runner_num in board[nx][ny]:
                runners[-runner_num] = False
                count += 1
            board[nx][ny] = 10
    return count, board, runners


def main():
    n, m, h, k = map(int, input().split())  # 크기, 도망자 수, 나무 수, 반복 횟수(턴 수)
    # 10: 빈칸, -i (0이하의 음수: 도망자, 'T': 나무
    board = [[10 for _ in range(n)] for _ in range(n)]
    order_list = get_order_list(n)
    runners = []
    answer = 0

    for i in range(m):
        x, y, d = map(int, input().split())
        if board[x-1][y-1] == 10:
            board[x-1][y-1] = [-i]
        else:
            board[x-1][y-1].append(-i)
        # d = 0 오른쪽 , d = 1 아래쪽, d = 2 왼쪽, d = 3 위쪽
        runners.append([x-1, y-1, d-1])

    for _ in range(h):
        x, y = map(int, input().split())
        board[x-1][y-1] = 'T'

    cx, cy, cd = n//2, n//2, 3
    for i in range(k):
        # 도망자 움직임
        runners, board = runner_move(runners, board, cx, cy)

        # 술래 다음 위치와 방향으로 설정
        cx, cy, cd = order_list[i % len(order_list)]  # 술래의 위치

        # 움직인 위치로부터 도망자 탐색
        catch_cnt, board, runners = scan(cx, cy, cd, board, runners)
        answer += (i+1) * catch_cnt

    print(answer)


main()
