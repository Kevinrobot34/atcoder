from collections import deque

h, w = map(int, input().split())
c = [list(input()) for _ in range(h)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

n = h * w
graph = [[] for _ in range(n)]
for i in range(h):
    for j in range(w):
        if c[i][j] == 's':
            v_start = i * w + j
        elif c[i][j] == 'g':
            v_goal = i * w + j
        for k in range(4):
            nx = i + dx[k]
            ny = j + dy[k]
            if nx < 0 or nx >= h or ny < 0 or ny >= w:
                continue
            v0 = i * w + j
            v1 = nx * w + ny
            cost = 1 if c[nx][ny] == '#' else 0
            graph[v0].append((cost, v1))

dist = [n + 1] * n
dist[v_start] = 0
q = deque([(0, v_start)])
while q:
    d, v = q.popleft()
    for cost, v_next in graph[v]:



ans = 'YES' if dist[v_goal] <= 2 else 'NO'
print(ans)
