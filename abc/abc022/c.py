def warshall_floyd(d):
    # d        : nxn adjacent matrix
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if d[i][j] > d[i][k] + d[k][j]:
                    d[i][j] = d[i][k] + d[k][j]


n, m = map(int, input().split())
INF = 10**10
edge = [[INF] * n for _ in range(n)]
for i in range(n):
    edge[i][i] = 0
for _ in range(m):
    u, v, l = map(int, input().split())
    u -= 1
    v -= 1
    edge[u][v] = l
    edge[v][u] = l
edge_zero = edge[0][:]
for i in range(1, n):
    edge[0][i] = INF
    edge[i][0] = INF

warshall_floyd(edge)

ans = INF
for x in range(1, n - 1):
    if edge_zero[x] == INF:
        continue
    for y in range(x + 1, n):
        if edge_zero[y] == INF:
            continue

        ans = min(ans, edge_zero[x] + edge[x][y] + edge_zero[y])

ans = ans if ans != INF else -1

print(ans)
