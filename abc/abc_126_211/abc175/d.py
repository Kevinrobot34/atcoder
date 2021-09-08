n, k = map(int, input().split())
p = list(map(lambda x: int(x) - 1, input().split()))
c = list(map(int, input().split()))

ans = -float('inf')
visited = [False] * n
for i in range(n):
    if not visited[i]:
        visited[i] = True
        loop = [i]
        cost = [c[i]]
        while not visited[p[loop[-1]]]:
            visited[p[loop[-1]]] = True
            cost.append(c[p[loop[-1]]])
            loop.append(p[loop[-1]])

        total_cost = sum(cost)
        # print(loop)
        # print(cost)
        # print(total_cost)

        m = len(loop)
        point = [-float('inf')] * m
        for j1 in range(m):
            s = 0
            for j2 in range(1, min(m, k) + 1):
                s += cost[(j1 + j2) % m]
                point[j1] = max(point[j1], s, s + total_cost * ((k - j2) // m))

        # print(point)
        ans = max(ans, max(point))

print(ans)
