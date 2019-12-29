n = int(input())


def concat_board(board1, board2):
    # クォリティーが同じ２つのboardを対角線上に配置して繋ぐ
    # A..
    # .BB
    # .BB
    x, y = len(board1), len(board2)
    board = []
    sr = '.' * y
    board += [board1[i] + sr for i in range(x)]
    sl = '.' * x
    board += [sl + board2[i] for i in range(y)]
    return board


def make3board(x):
    # 3x3のクォリティー2の敷き詰め方
    # aab
    # d.b
    # dcc
    base = ["aab", "d.b", "dcc"]
    if x == 3:
        return base
    else:
        return concat_board(base, make3board(x - 3))


def make4board(x):
    # 4x4のクォリティー3の敷き詰め方
    # aagh
    # bbgh
    # cdee
    # cdff
    base = ["aagh", "bbgh", "cdee", "cdff"]
    if x == 4:
        return base
    else:
        return concat_board(base, make4board(x - 4))


def make5board(x):
    # 5x5のクォリティー3の敷き詰め方
    # aadde
    # bbg.e
    # ccgff
    # ..abc
    # ..abc
    base = ["aadde", "bbg.e", "ccgff", "..abc", "..abc"]
    if x == 5:
        return base
    else:
        return concat_board(base, make5board(x - 5))


board = []
if n % 3 == 0:
    board = make3board(n)
elif n % 4 == 0:
    board = make4board(n)
elif n % 5 == 0:
    board = make5board(n)
elif n == 7 or n == 11:
    board = [
        "aabbcc.", "dd.dd.c", "..d..dc", "..d..db", "dd.dd.b", "..d..da",
        "..d..da"
    ]
    if n == 11:
        board = concat_board(board, make4board(4))
else:
    for x in range(4, n, 4):
        y = n - x
        if y % 5 == 0:
            board = concat_board(make4board(x), make5board(y))
            break

if len(board) != 0:
    print(*board, sep='\n')
else:
    print(-1)
