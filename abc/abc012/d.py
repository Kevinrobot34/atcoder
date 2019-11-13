import sys
input = sys.stdin.readline
INF = 10**8


def warshall_floyd(d):
    # d        : nxn adjacent matrix
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if d[i][j] > d[i][k] + d[k][j]:
                    d[i][j] = d[i][k] + d[k][j]


n, m = map(int, input().split())
d = [[INF] * n for _ in range(n)]
for i in range(n):
    d[i][i] = 0
for _ in range(m):
    a, b, t = map(int, input().split())
    a -= 1
    b -= 1
    d[a][b] = t
    d[b][a] = t

warshall_floyd(d)

d_max = [max(d[i]) for i in range(n)]
ans = min(d_max)

print(ans)
