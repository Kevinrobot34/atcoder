n, m = map(int, input().split())
h = tuple(map(int, input().split()))
graph = [[] for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    graph[a].append(b)
    graph[b].append(a)

ans = 0
for i in range(n):
    is_good = True
    for v in graph[i]:
        if h[i] <= h[v]:
            is_good = False
            break
    if is_good:
        ans += 1

print(ans)
