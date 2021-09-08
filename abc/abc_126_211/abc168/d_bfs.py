from collections import deque
n, m = map(int, input().split())

graph = [[] for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    graph[a].append(b)
    graph[b].append(a)

dist = [-1] * n
prev_node = [-1] * n
dist[0] = 0
q = deque([0])
while q:
    v = q.popleft()
    for v_next in graph[v]:
        if dist[v_next] == -1:
            dist[v_next] = dist[v] + 1
            prev_node[v_next] = v
            q.append(v_next)

# print(dist)
# print(prev_node)

print('Yes')
for i in range(1, n):
    print(prev_node[i] + 1)
