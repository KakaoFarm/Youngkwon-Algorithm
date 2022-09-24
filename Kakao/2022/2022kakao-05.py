board = [["" for _ in range(51)] for _ in range(51)]
merge_index = [[-1 for _ in range(51)] for _ in range(51)]
merge_table = []


def solution(commands):
    answer = []
    for comm in commands:
        c_list = comm.split()
        if c_list[0] == 'UPDATE':
            if len(c_list) == 4:
                r, c, value = c_list[1:]
                r, c = int(r), int(c)
                mi = merge_index[r][c]
                if mi == -1:
                    board[r][c] = value
                else:
                    for (a, b) in merge_table[mi]:
                        board[a][b] = value
            else:
                value1, value2 = c_list[1:]
                for i in range(51):
                    for j in range(51):
                        if board[i][j] == value1:
                            mi = merge_index[i][j]
                            if mi == -1:
                                board[i][j] = value2
                            else:
                                for (a, b) in merge_table[mi]:
                                    board[a][b] = value2

        if c_list[0] == 'MERGE':
            r1, c1, r2, c2 = map(int, c_list[1:])
            if board[r1][c1] != "" and board[r2][c2] != "":
                board[r2][c2] = board[r1][c1]
            elif board[r1][c1] != "" and board[r2][c2] == "":
                board[r2][c2] = board[r1][c1]
            elif board[r2][c2] != "" and board[r1][c1] == "":
                board[r1][c1] = board[r2][c2]

            # 둘다 merge되지 않은 상태
            if merge_index[r1][c1] == -1 and merge_index[r2][c2] == -1:
                mi = len(merge_table)
                merge_index[r1][c1] = mi
                merge_index[r2][c2] = mi
                merge_table.append([(r1, c1), (r2, c2)])
            # 둘중 하나만 merge인 상태
            elif (merge_index[r1][c1] != -1 and merge_index[r2][c2] == -1):
                mi = merge_index[r1][c1]
                merge_index[r2][c2] = mi
                merge_table[mi].append((r2, c2))

            elif (merge_index[r1][c1] == -1 and merge_index[r2][c2] != -1):
                mi = merge_index[r2][c2]
                merge_index[r1][c1] = mi
                merge_table[mi].append((r1, c1))
            # 둘다 merge 상태
            elif merge_index[r1][c1] != -1 and merge_index[r2][c2] != -1:
                mi1 = merge_index[r1][c1]
                mi2 = merge_index[r2][c2]
                for a, b in merge_table[mi2]:
                    board[a][b] = board[r1][c1]
                    merge_index[a][b] = mi1
                    merge_table[mi1].append((a, b))
                merge_table[mi2] = []

        if c_list[0] == 'UNMERGE':
            r, c = map(int, c_list[1:])
            mi = merge_index[r][c]
            temp_mi = mi
            for a, b in merge_table[mi]:
                if (a, b) != (r, c):
                    board[a][b] = ""
                merge_index[a][b] = -1
            merge_table[temp_mi] = []

        if c_list[0] == 'PRINT':
            r, c = map(int, c_list[1:])
            answer.append(
                board[r][c]) if board[r][c] != '' else answer.append("EMPTY")

    return answer
