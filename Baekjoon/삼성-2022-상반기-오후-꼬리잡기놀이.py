#
# 삼성 SW 역량 평가 - 2022 상반기 오후 - 꼬리잡기놀이
# 구현, 시뮬레이션
#

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]


# track 구하는 함수
def dfs(i, j, board, track, visited, order, track_num):
    limit = range(len(board))
    visited[i][j] = True
    value = board[i][j]
    if board[i][j] == 4:
        board[i][j] = [-1, track_num]
        track.append([i, j, -1])
    else:
        board[i][j] = [order, track_num]
        track.append([i, j, order])

    for d in range(4):
        ni = i + dx[d]
        nj = j + dy[d]
        if ni in limit and nj in limit and not visited[ni][nj] and board[ni][nj] != 0 and board[ni][nj] in [value, value + 1]:
            board, track = dfs(ni, nj, board, track,
                               visited, order + 1, track_num)

    return board, track


# 움직이기 함수
def move(tracks, board):
    new_tracks = []
    for track in tracks:
        temp_track = [track[-1]] + [each[:] for each in track]
        for i in range(len(track)):
            temp_track[i][2] = temp_track[i+1][2]
            x, y, p = temp_track[i]
            board[x][y] = [p, board[x][y][1]]
        new_tracks.append(temp_track[:-1])
    return new_tracks, board


# track_num 번째 Track 순서 뒤집기
def reverse_track(tracks, track_num):
    new_tracks = []
    for i in range(len(tracks)):
        if i != track_num:
            new_tracks.append(tracks[i])
        else:
            track = tracks[i]
            if track[-1][2] == -1:
                reverse_track = []
                cut_index = 0
                for ti in range(len(track)):
                    if track[ti][2] == -1:
                        cut_index = ti-1
                        break
                for k in range(cut_index, -1, -1):
                    order = (cut_index + 2) - track[k][2]
                    reverse_track.append([track[k][0], track[k][1], order])
                for k in range(len(track)-1, cut_index, -1):
                    reverse_track.append([track[k][0], track[k][1], -1])
                new_tracks.append(reverse_track)
            else:
                reverse_track = [each[:] for each in track]
                for ti in range(len(track) // 2):
                    reverse_track[ti], reverse_track[len(
                        track)-1-ti] = reverse_track[len(track)-1-ti][0:2]+[track[ti][2]], track[ti][0:2] + [track[len(track)-1-ti][2]]
                new_tracks.append(reverse_track)
    return new_tracks


# 공 던지기 함수
def throw(_round, tracks, board):
    n = len(board)
    point = 0
    direction = (_round // n) % 4
    index = _round % n

    if direction == 0:  # 좌측에서 던지기
        for i in range(n):
            if board[index][i] != 0 and board[index][i][0] > 0:
                point = (board[index][i][0] ** 2)
                tracks = reverse_track(tracks, board[index][i][1])
                break
    elif direction == 1:  # 아래에서 던지기
        for i in range(n-1, -1, -1):
            if board[i][index] != 0 and board[i][index][0] > 0:
                point = (board[i][index][0] ** 2)
                tracks = reverse_track(tracks, board[i][index][1])
                break
    elif direction == 2:  # 우측에서 던지기
        for i in range(n-1, -1, -1):
            if board[n-1-index][i] != 0 and board[n-1-index][i][0] > 0:
                point = (board[n-1-index][i][0] ** 2)
                tracks = reverse_track(tracks, board[n-1-index][i][1])
                break
    elif direction == 3:  # 위에서 던지기
        for i in range(n):
            if board[i][n-1-index] != 0 and board[i][n-1-index][0] > 0:
                point = (board[i][n-1-index][0] ** 2)
                tracks = reverse_track(tracks, board[i][n-1-index][1])
                break

    return tracks, point


def main():
    n, m, k = map(int, input().split())

    board = [list(map(int, input().split())) for _ in range(n)]
    answer = 0

    # tracks 구하기
    tracks = []
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:  # 머리사람을 발견하면 track 계산
                visited = [[False for _ in range(n)] for _ in range(n)]
                board, track = dfs(i, j, board, [], visited, 1, len(tracks))
                tracks.append(track)

    for _round in range(k):
        # move
        tracks, board = move(tracks, board)

        # 공 던지기
        tracks, point = throw(_round, tracks, board)

        answer += point

    print(answer)


main()
