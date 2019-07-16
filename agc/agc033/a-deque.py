from collections import deque
h, w = map(int, input().split())
a = ['#' * (w+2)] + ['#' + input() + '#' for i in range(h)] + ['#' * (w+2)]
for i in range(h+2):
    a[i] = list(a[i])

d = [(1, 0), (0, 1), (-1, 0), (0, -1)]
q = deque([])
for i in range(1, h+1):
    for j in range(1, w+1):
        if a[i][j] == '#':
            q.append((i, j, 0))

ans = 0
while q:
    i, j, c = q.popleft()
    for di, dj in d:
        if a[i+di][j+dj] == '.':
            a[i+di][j+dj] = '#'
            q.append((i+di, j+dj, c+1))
    ans = max(ans, c)

print(ans)
