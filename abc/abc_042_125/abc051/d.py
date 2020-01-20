def warshall_floyd(d, next_node):
    # d: nxn adjacent matrix
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if d[i][j] > d[i][k] + d[k][j]:
                    d[i][j] = d[i][k] + d[k][j]
                    next_node[i][j] = next_node[i][k]


INF = float("inf")

n, m = map(int, input().split())
d = [[INF] * n for _ in range(n)]
next_node = [list(range(n)) for _ in range(n)]
for i in range(n):
    d[i][i] = 0
for j in range(m):
    a, b, c = map(int, input().split())
    a, b = a - 1, b - 1
    d[a][b] = d[b][a] = c

warshall_floyd(d, next_node)

used_path = set()
for i in range(n):
    for j in range(n):
        if i == j:
            continue
        used_path.add((i, next_node[i][j]))
        used_path.add((next_node[i][j], i))

ans = m - len(used_path) // 2

print(ans)
