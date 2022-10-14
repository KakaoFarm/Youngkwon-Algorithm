#
# Baekjoon 20057 - 마법사 상어와 토네이도
# Gold 3
# 구현, 시뮬레이션
#

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]
answer = 0


# 토네이도 이동
def move(board, nx, ny, d):
    global answer

    sand = board[nx][ny]
    moved = 0
    area_range = range(len(board))

    # 좌측으로 이동
    if d == 0:
        # 1%, 7%, 10%
        for x in (nx - 1, nx + 1):
            for y in (ny - 1, ny, ny + 1):

                move_sand = 0
                if y == ny - 1:
                    move_sand = int(0.1 * sand)
                elif y == ny:
                    move_sand = int(0.07 * sand)
                elif y == ny + 1:
                    move_sand = int(0.01 * sand)

                if x in area_range and y in area_range:
                    board[x][y] += move_sand
                else:
                    answer += move_sand
                moved += move_sand

        # 2%
        for x in (nx - 2, nx + 2):
            move_sand = int(0.02 * sand)
            if x in area_range:
                board[x][ny] += move_sand
            else:
                answer += move_sand
            moved += move_sand

        # 5%
        y = (ny - 2)
        move_sand = int(0.05 * sand)
        if y in area_range:
            board[nx][y] += move_sand
        else:
            answer += move_sand
        moved += move_sand

        # alpha
        y = (ny - 1)
        move_sand = sand - moved
        if y in area_range:
            board[nx][y] += move_sand
        else:
            answer += move_sand

    # 아래로 이동
    if d == 1:
        # 1%, 7%, 10%
        for y in (ny - 1, ny + 1):
            for x in (nx - 1, nx, nx + 1):

                move_sand = 0
                if x == nx - 1:
                    move_sand = int(0.01 * sand)
                elif x == nx:
                    move_sand = int(0.07 * sand)
                elif x == nx + 1:
                    move_sand = int(0.1 * sand)

                if x in area_range and y in area_range:
                    board[x][y] += move_sand
                else:
                    answer += move_sand
                moved += move_sand

        # 2%
        for y in (ny - 2, ny + 2):
            move_sand = int(0.02 * sand)
            if y in area_range:
                board[nx][y] += move_sand
            else:
                answer += move_sand
            moved += move_sand

        # 5%
        x = (nx + 2)
        move_sand = int(0.05 * sand)
        if x in area_range:
            board[x][ny] += move_sand
        else:
            answer += move_sand
        moved += move_sand

        # alpha
        x = (nx + 1)
        move_sand = sand - moved
        if x in area_range:
            board[x][ny] += move_sand
        else:
            answer += move_sand

    # 우측으로 이동
    if d == 2:
        # 1%, 7%, 10%
        for x in (nx - 1, nx + 1):
            for y in (ny - 1, ny, ny + 1):

                move_sand = 0
                if y == ny - 1:
                    move_sand = int(0.01 * sand)
                elif y == ny:
                    move_sand = int(0.07 * sand)
                elif y == ny + 1:
                    move_sand = int(0.1 * sand)

                if x in area_range and y in area_range:
                    board[x][y] += move_sand
                else:
                    answer += move_sand
                moved += move_sand

        # 2%
        for x in (nx - 2, nx + 2):
            move_sand = int(0.02 * sand)
            if x in area_range:
                board[x][ny] += move_sand
            else:
                answer += move_sand
            moved += move_sand

        # 5%
        y = (ny + 2)
        move_sand = int(0.05 * sand)
        if y in area_range:
            board[nx][y] += move_sand
        else:
            answer += move_sand
        moved += move_sand

        # alpha
        y = (ny + 1)
        move_sand = sand - moved
        if y in area_range:
            board[nx][y] += move_sand
        else:
            answer += move_sand

    # 위로 이동
    if d == 3:
        # 1%, 7%, 10%
        for y in (ny - 1, ny + 1):
            for x in (nx - 1, nx, nx + 1):

                move_sand = 0
                if x == nx - 1:
                    move_sand = int(0.1 * sand)
                elif x == nx:
                    move_sand = int(0.07 * sand)
                elif x == nx + 1:
                    move_sand = int(0.01 * sand)

                if x in area_range and y in area_range:
                    board[x][y] += move_sand
                else:
                    answer += move_sand
                moved += move_sand

        # 2%
        for y in (ny - 2, ny + 2):
            move_sand = int(0.02 * sand)
            if y in area_range:
                board[nx][y] += move_sand
            else:
                answer += move_sand
            moved += move_sand

        # 5%
        x = nx - 2
        move_sand = int(0.05 * sand)
        if x in area_range:
            board[x][ny] += move_sand
        else:
            answer += move_sand
        moved += move_sand

        # alpha
        x = nx - 1
        move_sand = sand - moved
        if x in area_range:
            board[x][ny] += move_sand
        else:
            answer += move_sand

    return board


# 토네이도가 움직인 후에, 방향을 바꿔야 하는지 확인
def get_new_d(visited, tx, ty, d):
    # 범위를 벗어날 일이 없음

    if d == 0:  # 왼쪽으로 이동
        if not visited[tx+1][ty]:
            return 1

    elif d == 1:  # 아래로 이동
        if not visited[tx][ty+1]:
            return 2

    elif d == 2:  # 오른쪽으로 이동
        if not visited[tx-1][ty]:
            return 3

    elif d == 3:  # 위로 이동
        if not visited[tx][ty-1]:
            return 0

    return d


def main():
    N = int(input())
    board = []
    for _ in range(N):
        board.append(list(map(int, input().split())))
    visited = [[False for _ in range(N)] for _ in range(N)]
    d = 0
    tx, ty = N // 2, N // 2

    while (tx, ty) != (0, 0):
        visited[tx][ty] = True
        tx = tx + dx[d]
        ty = ty + dy[d]
        board = move(board, tx, ty, d)
        d = get_new_d(visited, tx, ty, d)

    print(answer)


main()
