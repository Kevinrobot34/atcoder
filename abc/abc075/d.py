import sys
from operator import itemgetter
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())
p = [list(map(int, input().split())) for _ in range(n)]
p.sort(key=itemgetter(0))

d = deque()
ans = float('INF')
for i in range(n):
    if len(d) < k:
        d.append(p[i])
    else:
        # len(d) == k
        _ = d.popleft()
        d.append(p[i])

    if len(d) < k:
        continue

    x_min, y_min = d[0]
    x_max, y_max = d[0]
    for j in range(1, len(d)):
        x, y = d[j]
        x_min = min(x_min, x)
        y_min = min(y_min, y)
        x_max = max(x_max, x)
        y_max = max(y_max, y)
    ans = min(ans, (x_max - x_min) * (y_max - y_min))


p.sort(key=itemgetter(1))
d = deque()
for i in range(n):
    if len(d) < k:
        d.append(p[i])
    else:
        # len(d) == k
        _ = d.popleft()
        d.append(p[i])

    if len(d) < k:
        continue

    x_min, y_min = d[0]
    x_max, y_max = d[0]
    for j in range(1, len(d)):
        x, y = d[j]
        x_min = min(x_min, x)
        y_min = min(y_min, y)
        x_max = max(x_max, x)
        y_max = max(y_max, y)
    ans = min(ans, (x_max - x_min) * (y_max - y_min))


print(ans)
