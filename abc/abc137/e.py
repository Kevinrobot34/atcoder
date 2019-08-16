n, m, p = map(int, input().split())
edge = []
for i in range(m):
    a, b, c = map(int, input().split())
    a -= 1
    b -= 1
    edge.append((a, b, -c+p))


INF = float('inf')
d = [INF] * n
d[0] = 0
for i in range(n):
    for v_from, v_to, cost in edge:
        if d[v_from] != INF and d[v_to] > d[v_from] + cost:
            d[v_to] = d[v_from] + cost


exist = True
for i in range(n):
    for v_from, v_to, cost in edge:
        if d[v_from] != INF and d[v_to] > d[v_from] + cost:
            d[v_to] = d[v_from] + cost
            if v_to == n - 1:
                exist = False

if not exist:
    print(-1)
else:
    print(max(0, -d[n-1]))
