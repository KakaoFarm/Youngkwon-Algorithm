#
# Baekjoon 21611 - 마법사 상어와 블리자드
# Gold 1
# 구현, 시뮬레이션
#

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
ball = [0, 0, 0, 0]


# 마법 (블리자드)
def do_magic(board, md, ms):
    x = len(board) // 2
    y = len(board) // 2
    for dist in range(1, ms + 1):
        nx = x + (dx[md] * dist)
        ny = y + (dy[md] * dist)
        if nx in range(len(board)) and ny in range(len(board)):
            board[nx][ny] = 0

    return board


# 탐색 번호 순서대로 인덱스 리스트 저장
def get_order_index_list(N):
    x, y = N//2, N//2 - 1
    d = 1
    visited = [[False for _ in range(N)] for _ in range(N)]
    visited[N//2][N//2] = True

    order_index_list = []
    while True:
        visited[x][y] = True
        order_index_list.append([x, y])

        if (x, y) == (0, 0):
            break

        x = x + dx[d]
        y = y + dy[d]

        if d == 1:  # 아래로 이동
            if not visited[x][y+1]:
                d = 3
        elif d == 3:  # 오른쪽으로 이동
            if not visited[x-1][y]:
                d = 0
        elif d == 0:  # 위로 이동
            if not visited[x][y-1]:
                d = 2
        elif d == 2:  # 왼쪽으로 이동
            if not visited[x+1][y]:
                d = 1
    return order_index_list


# 구슬 이동
def move(board, order_index_list):
    zero_count = 0
    for i in range(len(order_index_list)):
        x, y = order_index_list[i]
        if board[x][y] == 0:
            zero_count += 1
        else:
            fast_x, fast_y = order_index_list[i-zero_count]
            board[fast_x][fast_y] = board[x][y]
            if zero_count > 0:
                board[x][y] = 0

    return board


# 구슬 폭발
def explosion(board, order_index_list):
    ball_num = 0
    stack = []
    exploded = False
    for i in range(len(order_index_list)):
        x, y = order_index_list[i]
        if board[x][y] != ball_num:
            if len(stack) >= 4:
                exploded = True
                for old_x, old_y in stack:
                    board[old_x][old_y] = 0
                    ball[ball_num] += 1
            ball_num = board[x][y]
            stack = [[x, y]]
        else:
            stack.append([x, y])

    return board, exploded


# 그룹별로 처리
def grouping(board, order_index_list):
    ball_num = 0
    stack = []
    groups = []
    for i in range(len(order_index_list)):
        x, y = order_index_list[i]

        if board[x][y] != ball_num and ball_num != 0:  # 초기 상태를 제외하고 Ball이 다를 때
            # groups[0] = [[1, 2], [2, 2], [3, 1], ... , [A, B]]의 형태
            groups.append([len(stack), ball_num])
            ball_num = board[x][y]
            stack = [[x, y]]
        else:
            ball_num = board[x][y]
            stack.append([x, y])

    new_board = [[0 for _ in range(len(board))] for _ in range(len(board))]
    index = 0
    for A, B in groups:
        gx, gy = order_index_list[index]
        new_board[gx][gy] = A
        index += 1
        if index >= len(order_index_list):
            break

        gx, gy = order_index_list[index]
        new_board[gx][gy] = B
        index += 1
        if index >= len(order_index_list):
            break
    return new_board


def main():
    N, M = map(int, input().split())
    board = []
    zero_board = [[0 for _ in range(N)] for _ in range(N)]
    magics = []
    order_index_list = get_order_index_list(N)

    for _ in range(N):
        board.append(list(map(int, input().split())))
    for _ in range(M):
        magic = list(map(int, input().split()))
        magics.append([magic[0]-1, magic[1]])

    # 마법 순차적으로 실행
    for mi in range(len(magics)):
        md, ms = magics[mi]

        # 마법 실행
        board = do_magic(board, md, ms)

        # 구슬 이동
        board = move(board, order_index_list)

        # 구슬 폭발 & 이동 반복 (더 이상 폭발하지 않을 때 까지)
        while True:
            # 구슬 폭발
            board, exploded = explosion(board, order_index_list)
            if not exploded:  # 더 이상 연속 4개 이상이 없어서 폭발하지 않으면 break
                break

            # 구슬 이동
            board = move(board, order_index_list)

        # 그룹별로 처리
        board = grouping(board, order_index_list)

        if board == zero_board:
            break

    # 정답 출력
    print(ball[1] + 2*ball[2] + 3*ball[3])


main()
