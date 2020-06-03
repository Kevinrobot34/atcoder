n, m = map(int, input().split())
b = [list(map(int, list(input()))) for _ in range(n)]

a = [[0] * m for _ in range(n)]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

for i in range(1, n - 1):
    for j in range(1, m - 1):
        bij_min = min(b[i + dx[k]][j + dy[k]] for k in range(4))
        if bij_min > 0:
            a[i][j] = bij_min
            for k in range(4):
                b[i + dx[k]][j + dy[k]] -= bij_min

for ai in a:
    print(''.join([str(aij) for aij in ai]))
