import sys
sys.setrecursionlimit(200_000)

n = int(input())
edge = [[] for _ in range(n)]
for i in range(n - 1):
    u, v, w = map(int, input().split())
    u -= 1
    v -= 1
    edge[u].append((v, w))
    edge[v].append((u, w))


visited = [0] * n
ans = [0] * n
def dfs(u, d):
    for i in range(len(edge[u])):
        v, w = edge[u][i]
        if visited[v] == 0:
            ans[v] = (d + w) % 2
            visited[v] = 1
            dfs(v, d + w)


visited[0] = 1
dfs(0, 0)
for a in ans:
    print(a)
