import sys
sys.setrecursionlimit(10**8)
MOD = 10**9 + 7

n = int(input())
graph = [[] for _ in range(n)]
for i in range(n - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    graph[a].append(b)
    graph[b].append(a)

black = [0] * n
white = [0] * n


def dfs(v, p):
    b, w = 1, 1
    for u in graph[v]:
        if u == p:
            continue
        dfs(u, v)
        b *= white[u]
        w *= black[u] + white[u]
        b %= MOD
        w %= MOD
    black[v] = b
    white[v] = w


dfs(0, -1)
ans = (black[0] + white[0]) % MOD
# print(black)
# print(white)
print(ans)
