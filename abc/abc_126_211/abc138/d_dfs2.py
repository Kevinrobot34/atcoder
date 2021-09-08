import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n, q = map(int, input().split())
edge = [[] for i in range(n)]
for i in range(n-1):
    a, b = map(int, input().split())
    a, b = a-1, b-1
    edge[a].append(b)
    edge[b].append(a)

imos = [0 for i in range(n)]
for i in range(q):
    p, x = map(int, input().split())
    p -= 1
    imos[p] += x

def dfs(v, p):
    for u in edge[v]:
        if u == p:
            continue
        imos[u] += imos[v]
        dfs(u, v)

dfs(0, -1)
print(' '.join([str(x) for x in imos]))
