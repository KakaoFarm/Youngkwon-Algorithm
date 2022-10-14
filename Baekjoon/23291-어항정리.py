#
# Baekjoon 23291 - 어항 정리
# Platinum 5
# 구현, 시뮬레이션
#


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


# 가장 왼쪽 열의 아래 행부터 맨 위 행까지의 값을 배열로 get
def get_pillow(_board, col):
    pillow = []
    for row in range(len(_board)-1, -1, -1):
        val = _board[row][col]
        if val == 0:
            break
        pillow.append(val)

    return pillow


# 가장 작은 값에 + 1
def minimum_add(_board):
    bottom = _board[-1]
    min_val = min(bottom)
    for i in range(len(bottom)):
        if bottom[i] == min_val:
            bottom[i] += 1
    _board[-1] = bottom
    return _board


def main():
    N, K = map(int, input().split())
    board = [[0 for _ in range(N)] for _ in range(N)]
    board.append(list(map(int, input().split())))  # N+1(행) x N(열)

    iii = 0
    answer = 0
    while True:  # 종료 조건 = 물고기 수 차이가 K 이하
        iii += 1
        answer += 1

        # 가장 작은 값에 + 1
        board = minimum_add(board)

        # 먼저 한번 접고
        board[-2][1] = board[-1][0]
        board[-1][0] = 0
        left_index = 1

        # 반복해서 접기
        while True:
            if board[-2][-1] != 0:
                break

            pillow_list = []

            for col in range(1, N):
                pillow = get_pillow(board, col)
                if len(pillow) > 1:  # 공중부양 대상(pillow list) 구하기
                    pillow_list.append(pillow)

            height = len(pillow_list[0])
            if left_index + len(pillow_list) + height > N:
                break

            for i in range(len(pillow_list)):  # pillow 공간 0으로 삭제
                col = left_index + i
                for j in range(1, height + 1):
                    board[-j][col] = 0

            left_index += len(pillow_list)

            for i in range(len(pillow_list)):  # 가장 좌측 기둥부터
                pillow = pillow_list[i]
                for j in range(height):
                    board[-1 - (len(pillow_list) - i)
                          ][left_index + j] = pillow[j]

        # 양 조절하기
        new_board = [each[:] for each in board]
        for x in range(N+1):
            for y in range(left_index, N):
                if board[x][y] != 0:
                    cnt = 0
                    for i in range(4):
                        nx = x + dx[i]
                        ny = y + dy[i]
                        if nx in range(N+1) and ny in range(N) and board[nx][ny] != 0:
                            d = abs(board[nx][ny] - board[x][y]) // 5
                            if board[nx][ny] > board[x][y]:
                                cnt += d
                            else:
                                cnt -= d
                    new_board[x][y] = board[x][y] + cnt

        # 다시 펼치기
        bottom = []
        for y in range(left_index, N):
            for x in range(-1, -N+1, -1):
                if new_board[x][y] == 0:
                    break
                bottom.append(new_board[x][y])
        board = [[0 for _ in range(N)] for _ in range(N)]
        board.append(bottom)

        # 두번 반으로 접기
        for i in range(N//2):
            board[-2][(N-1)-i] = board[-1][i]
            board[-1][i] = 0

        for i in range(N//2, 3*N//4):
            board[-3][(N-1)-i + N//2] = board[-2][i]
            board[-4][(N-1)-i + N//2] = board[-1][i]
            board[-2][i] = 0
            board[-1][i] = 0

        # 다시 양 조절하기
        new_board = [each[:] for each in board]
        for x in range(N-3, N+1):
            for y in range(3*N//4, N):
                if board[x][y] != 0:
                    cnt = 0
                    for i in range(4):
                        nx = x + dx[i]
                        ny = y + dy[i]
                        if nx in range(N+1) and ny in range(N) and board[nx][ny] != 0:
                            d = abs(board[nx][ny] - board[x][y]) // 5
                            if board[nx][ny] > board[x][y]:
                                cnt += d
                            else:
                                cnt -= d
                    new_board[x][y] = board[x][y] + cnt

        # 다시 펼치기
        bottom = []
        for y in range(3*N//4, N):
            for x in range(-1, -(N+1), -1):
                if new_board[x][y] == 0:
                    break
                bottom.append(new_board[x][y])

        if max(bottom) - min(bottom) <= K:
            print(answer)
            break

        board = [[0 for _ in range(N)] for _ in range(N)]
        board.append(bottom)


main()
