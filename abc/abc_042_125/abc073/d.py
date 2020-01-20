from itertools import permutations


def warshall_floyd(d):
    # d        : nxn adjacent matrix
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if d[i][j] > d[i][k] + d[k][j]:
                    d[i][j] = d[i][k] + d[k][j]


INF = float("inf")

n, m, r = map(int, input().split())
r_list = list(map(lambda x: int(x) - 1, input().split()))
d = [[INF] * n for _ in range(n)]
for i in range(n):
    d[i][i] = 0
for i in range(m):
    a, b, c = map(int, input().split())
    a, b = a - 1, b - 1
    d[a][b] = d[b][a] = c
warshall_floyd(d)

ans = float("inf")
for np in permutations(r_list):
    cand = sum([d[np[i]][np[i + 1]] for i in range(r - 1)])
    ans = min(ans, cand)

print(ans)
