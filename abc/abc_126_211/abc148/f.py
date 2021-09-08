import sys
sys.setrecursionlimit(10**8)
input = sys.stdin.readline

n, u, v = map(int, input().split())
u, v = u - 1, v - 1
graph = [[] for _ in range(n)]
for _ in range(n - 1):
    a, b = map(int, input().split())
    a, b = a - 1, b - 1
    graph[a].append(b)
    graph[b].append(a)


def dfs(v, d, count):
    count[v] = d
    for v_next in graph[v]:
        if count[v_next] >= 0:
            continue
        dfs(v_next, d + 1, count)


count_tak = [-1] * n
dfs(u, 0, count_tak)
count_aok = [-1] * n
dfs(v, 0, count_aok)

ans = 0
for i in range(n):
    if count_tak[i] < count_aok[i]:
        ans = max(ans, count_aok[i] - 1)

print(ans)
