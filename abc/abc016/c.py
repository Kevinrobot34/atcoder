from collections import deque
n, m = map(int, input().split())
edge = [[] for _ in range(n)]
for i in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    edge[a].append(b)
    edge[b].append(a)


def bfs(a):
    INF = 10**10
    visited = [INF] * n
    visited[a] = 0
    queue = deque([(a, 0)])
    while queue:
        v, depth = queue.popleft()
        if depth >= 2:
            continue

        for u in edge[v]:
            if visited[u] != INF:
                continue
            else:
                visited[u] = depth + 1
                queue.append((u, depth + 1))

    res = 0
    for i in range(n):
        if visited[i] == 2:
            res += 1

    # print(a, res, visited)
    return res

for i in range(n):
    print(bfs(i))
