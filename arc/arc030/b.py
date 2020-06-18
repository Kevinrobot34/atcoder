n, x = map(int, input().split())
x -= 1
h = list(map(int, input().split()))
graph = [[] for _ in range(n)]
for _ in range(n - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    graph[a].append(b)
    graph[b].append(a)


def dfs(v, v_p):
    cost = 0
    for v_next in graph[v]:
        if v_next == v_p:
            continue
        cost_i = dfs(v_next, v)
        if cost_i > 0 or h[v_next] == 1:
            cost += cost_i + 2
    return cost


ans = dfs(x, -1)
print(ans)
