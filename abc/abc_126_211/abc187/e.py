import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)

n = int(input())
graph = [[] for _ in range(n)]
ab = []

for _ in range(n - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    graph[a].append(b)
    graph[b].append(a)
    ab.append((a, b))

v_root = 0
imos = [0] * n
depth = [0] * n
ans = [0] * n


def dfs1(v, v_par):
    for v_chi in graph[v]:
        if v_chi == v_par:
            continue
        depth[v_chi] = depth[v] + 1
        dfs1(v_chi, v)


def dfs2(v, v_par):
    ans[v] += imos[v]
    for v_chi in graph[v]:
        if v_chi == v_par:
            continue
        imos[v_chi] += imos[v]
        dfs2(v_chi, v)


dfs1(0, -1)
q = int(input())
for _ in range(q):
    t, e, x = map(int, input().split())
    e -= 1
    a, b = ab[e]
    if t == 2:
        a, b = b, a

    if depth[a] < depth[b]:
        imos[v_root] += x
        imos[b] -= x
    else:
        imos[a] += x

dfs2(v_root, -1)
print(*ans, sep='\n')
