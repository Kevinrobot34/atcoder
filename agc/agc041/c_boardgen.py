import random
char_list = 'abcdefghijklmnopqrstuvwxyz' + '0123456789' + '!@#$^&*({['


def print_board(board):
    q = calc_quality(board)
    print("size    :", len(board))
    print("quality :", q)
    print(*[''.join(board_i) for board_i in board], sep='\n')


def calc_quality(board):
    n = len(board)

    def count_char(s):
        char_set = set(s)
        char_set -= set('.')
        return len(char_set)

    q = count_char([board[0][j] for j in range(n)])
    for i in range(1, n):
        q_i = count_char([board[i][j] for j in range(n)])
        if q != q_i:
            return -1
    for i in range(n):
        q_i = count_char([board[j][i] for j in range(n)])
        if q != q_i:
            return -1
    return q


def board_generator(n, r_th=0.3):
    # generate a board whose size is n x n
    board = [['.'] * n for _ in range(n)]
    cnt_tile = 0
    for i in range(n):
        for j in range(n - 1):
            if board[i][j] != '.' or board[i][j + 1] != '.':
                continue
            r = random.random()
            if r < r_th:
                board[i][j] = char_list[cnt_tile]
                board[i][j + 1] = char_list[cnt_tile]
                cnt_tile += 1
    for i in range(n - 1):
        for j in range(n):
            if board[i][j] != '.' or board[i + 1][j] != '.':
                continue
            r = random.random()
            if r < r_th:
                board[i][j] = char_list[cnt_tile]
                board[i + 1][j] = char_list[cnt_tile]
                cnt_tile += 1

    return board


def board_generator2(n, q, r_th=0.3):
    # generate a board whose size is n x n
    board = [['.'] * n for _ in range(n)]
    cnt_tile = 0

    def count_char(s):
        char_set = set(s)
        char_set -= set('.')
        return len(char_set)

    for i in range(n):
        for j in range(n):
            if board[i][j] != '.':
                continue
            r = random.random()
            if r < r_th:
                if random.random() < 0.5:
                    if i < n - 1 and board[i + 1][j] == '.':
                        board[i][j] = char_list[cnt_tile]
                        board[i + 1][j] = char_list[cnt_tile]
                        cnt_tile += 1
                else:
                    if j < n - 1 and board[i][j + 1] == '.':
                        board[i][j] = char_list[cnt_tile]
                        board[i][j + 1] = char_list[cnt_tile]
                        cnt_tile += 1
        if count_char(board[i]) != q:
            # 行のクオリティーがおかしかったらやめる
            return []
    return board


def generator_fast(n, q, r_th=0.3, cnt_max=10000):
    # generate a board whose size is n x n
    board = [['.'] * n for _ in range(n)]
    cnt_trial = 0
    while cnt_trial < cnt_max:
        board = board_generator2(n, q, r_th=r_th)
        if len(board) == n and calc_quality(board) == q:
            print_board(board)
            break
        cnt_trial += 1
    print("TRIAL was FINISHED")


generator_fast(5, 3, r_th=0.5, cnt_max=1000000)
generator_fast(6, 3, r_th=0.5, cnt_max=1000000)
generator_fast(7, 3, r_th=0.3, cnt_max=1000000)


def generator_slow(n, q_target=-1, cnt_max=10000, r_th=0.3):
    cnt = 0
    while cnt < cnt_max:
        board = board_generator(n, r_th=r_th)
        q = calc_quality(board)
        if q == q_target:
            print_board(board)
            break
        cnt += 1
    print("TRIAL was FINISHED")


generator_slow(5, 3, r_th=0.5, cnt_max=1000000)
generator_slow(6, 3, r_th=0.5, cnt_max=1000000)
