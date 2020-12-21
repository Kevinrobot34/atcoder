from heapq import heappush, heappop

n = int(input())
graph = [[] for _ in range(n)]
for _ in range(n - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    graph[a].append(b)
    graph[b].append(a)

is_visited = [False] * n
ans = []
q = [0]
is_visited[0] = True
while q:
    v = heappop(q)
    ans.append(v + 1)
    for u in graph[v]:
        if is_visited[u]:
            continue
        heappush(q, u)
        is_visited[u] = True

print(*ans)
