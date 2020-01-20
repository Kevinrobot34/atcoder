n, m = map(int, input().split())
edge = [[] for i in range(n)]
for i in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    edge[a].append(b)
    edge[b].append(a)

visited = [0] * n
def dfs(v, p):
    if sum(visited) == n:
        return 1
    res = 0
    for u in edge[v]:
        if u != p and visited[u] == 0:
            visited[u] = 1
            res += dfs(u, v)
            visited[u] = 0
    return res

visited[0] = 1
ans = dfs(0, -1)

print(ans)
