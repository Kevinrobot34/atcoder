import sys
input = sys.stdin.readline

n, m, q = map(int, input().split())
graph = [[] for _ in range(n)]
for _ in range(m):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    graph[u].append(v)
    graph[v].append(u)
color = list(map(int, input().split()))

for _ in range(q):
    query = input()
    if query[0] == '1':
        _, x = map(int, query.split())
        x -= 1

        c = color[x]
        print(c)
        for u in graph[x]:
            color[u] = c
    else:
        _, x, y = map(int, query.split())
        x -= 1

        c = color[x]
        print(c)
        color[x] = y
