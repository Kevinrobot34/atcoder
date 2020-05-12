b = [list(map(int, input().split())) for _ in range(2)]
c = [list(map(int, input().split())) for _ in range(3)]


def calc(board):
    a = [['o'] * 3 for _ in range(3)]
    for i in range(9):
        if i % 2 == 1:
            a[board[i] // 3][board[i] % 3] = 'x'
    p1 = p2 = 0
    for i in range(2):
        for j in range(3):
            if a[i][j] == a[i + 1][j]:
                p1 += b[i][j]
            else:
                p2 += b[i][j]
    for i in range(3):
        for j in range(2):
            if a[i][j] == a[i][j + 1]:
                p1 += c[i][j]
            else:
                p2 += c[i][j]

    return p1, p2


def dfs(board):
    # print(board)
    if len(board) == 9:
        return calc(board)

    board_set = set(board)
    p1, p2 = -1, -1
    for i in range(9):
        if i in board_set:
            continue
        board.append(i)
        q1, q2 = dfs(board)
        board.pop()
        if len(board) % 2 == 0:
            if p1 < q1:
                p1, p2 = q1, q2
        else:
            if p2 < q2:
                p1, p2 = q1, q2
    return p1, p2


p1, p2 = dfs([])
print(p1)
print(p2)
