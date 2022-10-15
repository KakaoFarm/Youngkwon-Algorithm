#
# 삼성 SW 역량 평가 - 2022 상반기 오전 - 예술성
# 구현, 시뮬레이션
#

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]


def get_group_dfs(i, j, board, visited, group, group_board, group_num):
    limit = range(len(board))
    visited[i][j] = True
    group.append([i, j])
    group_board[i][j] = group_num
    for d in range(4):
        ni = i + dx[d]
        nj = j + dy[d]
        if ni in limit and nj in limit and not visited[ni][nj] and board[i][j] == board[ni][nj]:
            get_group_dfs(ni, nj, board, visited,
                          group, group_board, group_num)
    return group


def get_group(board):
    n = len(board)
    visited = [[False for _ in range(n)] for _ in range(n)]
    group_board = [[False for _ in range(n)] for _ in range(n)]
    groups = []  # [[1, [0, 0]], [2, [1, 0], [1, 1], ...],]
    group_num = 0
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                group = get_group_dfs(
                    i, j, board, visited, [], group_board, group_num)
                groups.append([board[i][j], len(group)])
                group_num += 1
    return groups, group_board


def get_point(groups, group_board, n):
    meet = {}
    limit = range(n)
    visited = [[False for _ in limit] for _ in limit]

    for i in limit:
        for j in limit:
            gn = group_board[i][j]
            for d in range(2, 4):  # 우측 하단만 탐색
                ni = i + dx[d]
                nj = j + dy[d]
                if ni in limit and nj in limit and group_board[i][j] != group_board[ni][nj]:
                    _key = (0, 0)
                    if group_board[i][j] < group_board[ni][nj]:
                        _key = (group_board[i][j], group_board[ni][nj])
                    else:
                        _key = (group_board[ni][nj], group_board[i][j])

                    if _key not in meet.keys():
                        meet[_key] = 1
                    else:
                        meet[_key] += 1

    point = 0
    for (g1, g2) in meet.keys():
        m = meet[(g1, g2)]
        g1_num = groups[g1][1]
        g2_num = groups[g2][1]
        g1_value = groups[g1][0]
        g2_value = groups[g2][0]
        point += (g1_num + g2_num) * g1_value * g2_value * m
    return point


# 십자모양 회전
def rotate_t(board):
    n = len(board)
    new_board = [each[:] for each in board]

    # 오른쪽을 위로
    for j in range((n//2)+1, n):
        new_board[n-1-j][n//2] = board[n//2][j]
    # 위쪽을 왼쪽으로
    for i in range(0, n//2):
        new_board[n//2][i] = board[i][n//2]
    # 왼쪽을 아래로
    for j in range(0, n//2):
        new_board[n-1-j][n//2] = board[n//2][j]
    # 아래를 오른쪽으로
    for i in range((n//2)+1, n):
        new_board[n//2][i] = board[i][n//2]

    return new_board


# 각 모퉁이 90도 회전
def rotate(board):
    n = len(board)
    new_board = [each[:] for each in board]
    small_n = (len(board) - 1) // 2

    # 좌상
    for i in range(n//2):
        for j in range(n//2):
            ni = j
            nj = (small_n - 1) - i
            new_board[ni][nj] = board[i][j]

    # 우상
    for i in range(n//2):
        for j in range(n//2 + 1, n):
            ni = j - (n//2 + 1)
            nj = (small_n - 1) - i + (n//2 + 1)
            new_board[ni][nj] = board[i][j]

    # 좌하
    for i in range(n//2 + 1, n):
        for j in range(n//2):
            ni = j + (n//2 + 1)
            nj = (small_n - 1) - i + (n//2 + 1)
            new_board[ni][nj] = board[i][j]

    # 우하
    for i in range(n//2 + 1, n):
        for j in range(n//2 + 1, n):
            ni = j
            nj = (small_n - 1) - i + 2*(n//2+1)
            new_board[ni][nj] = board[i][j]

    return new_board


def main():
    point = 0

    n = int(input())
    board = [list(map(int, input().split())) for _ in range(n)]

    # 그룹 구하기, [[[0, 0]], [[0, 1], [0, 2], ...], ...]
    groups, group_board = get_group(board)

    # point 구하기
    point += get_point(groups, group_board, n)

    for r in range(3):

        # 십자모양 회전
        board = rotate_t(board)

        # 시계방향 90도 회전
        board = rotate(board)

        # 그룹 구하기
        groups, group_board = get_group(board)

        # point 구하기
        point += get_point(groups, group_board, n)

    print(point)


main()
