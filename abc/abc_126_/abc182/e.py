h, w, n, m = map(int, input().split())

board = [[0] * (w + 2) for _ in range(h + 2)]

board[0] = [2] * (w + 2)
board[h + 1] = [2] * (w + 2)
for i in range(h + 2):
    board[i][0] = 2
    board[i][w + 1] = 2

for i in range(n):
    a, b = map(int, input().split())
    board[a][b] = 1

for i in range(m):
    c, d = map(int, input().split())
    board[c][d] = 2

# print(*board, sep='\n')
# print()

for i in range(1, h + 1):
    for j in range(1, w + 1):
        if board[i][j] == 0 and board[i][j - 1] in [1, 3]:
            board[i][j] = 3
    for j in reversed(range(1, w + 1)):
        if board[i][j] == 0 and board[i][j + 1] in [1, 3]:
            board[i][j] = 3

for j in range(1, w + 1):
    for i in range(1, h + 1):
        if board[i][j] in [0, 3] and board[i - 1][j] in [1, 4]:
            board[i][j] = 4
    for i in reversed(range(1, h + 1)):
        if board[i][j] in [0, 3] and board[i + 1][j] in [1, 4]:
            board[i][j] = 4
# print(*board, sep='\n')

ans = 0
for i in range(1, h + 1):
    for j in range(1, w + 1):
        if board[i][j] in [1, 3, 4]:
            ans += 1

print(ans)
