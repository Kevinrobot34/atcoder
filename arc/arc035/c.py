import sys
input = sys.stdin.readline

INF = 10**8
n, m = map(int, input().split())
d = [[INF] * n for _ in range(n)]
for i in range(n):
    d[i][i] = 0
for _ in range(m):
    a, b, c = map(int, input().split())
    a -= 1
    b -= 1
    d[a][b] = c
    d[b][a] = c

# warshall-floyd
for k in range(n):
    for i in range(n):
        for j in range(i + 1, n):
            if d[i][j] > d[i][k] + d[k][j]:
                d[i][j] = d[i][k] + d[k][j]
                d[j][i] = d[i][j]

s = 0
for i in range(n):
    for j in range(i + 1, n):
        s += d[i][j]

k = int(input())
for _ in range(k):
    x, y, z = map(int, input().split())
    x -= 1
    y -= 1
    if d[x][y] > z:
        d[x][y] = z
        d[y][x] = z
        s = 0
        for i in range(n):
            for j in range(i + 1, n):
                d[i][j] = min(d[i][j], d[i][x] + z + d[y][j],
                              d[i][y] + z + d[x][j])
                d[j][i] = d[i][j]

                s += d[i][j]

    print(s)
