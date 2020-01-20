import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n)]
for i in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    graph[a].append(b)

dist = [[-1] * n for _ in range(n)]
for i in range(n):
    queue = deque([(i, 0)])
    while queue:
        v, c = queue.popleft()
        for v_next in graph[v]:
            if dist[i][v_next] == -1:
                dist[i][v_next] = c + 1
                queue.append((v_next, c+1))

# print(dist)
ans_len = n + 1
for i in range(n):
    if dist[i][i] != -1:
        ans_len = min(ans_len, dist[i][i])
if ans_len == n + 1:
    print(-1)
else:
    for i in range(n):
        if dist[i][i] == ans_len:
            start_v = i
            break

    dist = [-1] * n
    prev_v = [-1] * n
    queue = deque([(start_v, 0)])
    while queue:
        v, c = queue.popleft()
        if v == start_v and c != 0:
            break
        for v_next in graph[v]:
            if dist[v_next] == -1:
                dist[v_next] = c + 1
                prev_v[v_next] = v
                queue.append((v_next, c+1))

    ans = []
    # print(start_v)
    # print(dist)
    # print(prev_v)
    v = start_v
    for i in range(ans_len):
        ans.append(v+1)
        v = prev_v[v]

    print(ans_len)
    print(*ans, sep='\n')
