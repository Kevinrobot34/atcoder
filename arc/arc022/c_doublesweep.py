import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)

n = int(input())
graph = [[] for _ in range(n)]
for _ in range(n - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    graph[a].append(b)
    graph[b].append(a)


def dfs(v, v_p):
    d, leaf = 0, v
    for v_next in graph[v]:
        if v_next == v_p:
            continue
        d_i, leaf_i = dfs(v_next, v)
        d_i += 1
        if d_i > d:
            d, leaf = d_i, leaf_i
    return d, leaf


_, ans0 = dfs(0, -1)
_, ans1 = dfs(ans0, -1)
ans0 += 1
ans1 += 1
print(ans0, ans1)
