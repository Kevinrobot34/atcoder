import sys
sys.setrecursionlimit(200000)
n = int(input())
edges = [[] for _ in range(n)]
for i in range(n-1):
    a, b, c = map(int, input().split())
    a -= 1
    b -= 1
    edges[a].append((b, c))
    edges[b].append((a, c))

q, k = map(int, input().split())
k -= 1

visited = [0] * n
d = [0] * n
def dfs(v, c):
    for u, c2 in edges[v]:
        if visited[u] == 0:
            d[u] = c + c2
            visited[u] = 1
            dfs(u, c + c2)

visited[k] = 1
dfs(k, 0)

for i in range(q):
    x, y = map(int, input().split())
    x -= 1
    y -= 1
    print(d[x] + d[y])
