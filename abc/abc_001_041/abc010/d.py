n, g, e = map(int, input().split())

m = 2 * n
graph = [[] for _ in range(m)]  # graph[v] = [(v_to, cost, rev), ...]
for i in range(1, n):
    graph[i].append((i + n - 1, 1, 0))
p = list(map(int, input().split()))
for pi in p:
    graph[pi + n - 1].append((m - 1, 1, 0))
for _ in range(e):
    a, b = map(int, input().split())
    if a > b:
        a, b = b, a
    # a < b
    if a == 0:
        graph[a].append((b, 1, 0))
        graph[b + n - 1].append((a, 1, 0))
    else:
        graph[a + n - 1].append((b, 1, 0))
        graph[b + n - 1].append((a, 1, 0))
