from collections import deque

n, q = map(int, input().split())
edge = [[] for _ in range(n)]
for i in range(n-1):
    a, b = map(int, input().split())
    a, b = a-1, b-1
    edge[a].append(b)
    edge[b].append(a)

imos = [0 for _ in range(n)]
for i in range(q):
    p, x = map(int, input().split())
    p -= 1
    imos[p] += x

dq = deque([(0, -1)])
while dq:
    v, p = dq.popleft()
    for u in edge[v]:
        if u == p:
            continue
        imos[u] += imos[v]
        dq.append((u, v))

print(' '.join([str(x) for x in imos]))
