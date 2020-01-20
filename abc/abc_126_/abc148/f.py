n, u, v = map(int, input().split())
u, v = u - 1, v - 1
graph = [[] for _ in range(n)]
for _ in range(n - 1):
    a, b = map(int, input().split())
    a, b = a - 1, b - 1
    graph[a].append(b)
    graph[b].append(a)

d_v = d_ = -1


def dfs(x, p, d, f_v):
    print(x, p, d, f_v)
    if x == v:
        d_v = d
        f_v = 1

    for y in graph[x]:
        if y == p:
            continue
        dfs(y, x, d + 1, f_v)


dfs(v, -1, 0, 1)
