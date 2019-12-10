n = int(input())
graph = [[] for _ in range(n)]
for i in range(n):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    graph[a].append(b)
    graph[b].append(a)


def dfs(v, p):
    for u in graph[v]:
        dfs(u, v)
