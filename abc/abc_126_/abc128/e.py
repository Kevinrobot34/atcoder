from heapq import heappush, heappop
from collections import deque
import sys
input = sys.stdin.readline

n, q = map(int, input().split())
event = []
stx = []
for i in range(n):
    s, t, x = map(int, input().split())
    heappush(event, (x - s - 0.5, +1, i))
    heappush(event, (x - t - 0.5, -1, i))
    stx.append((s, t, x))

for i in range(q):
    d = int(input())
    heappush(event, (d, 0, i))

ans = [-1] * q
queue = []  # [(t, x)]

while event:
    d, k, i = heappop(event)
    # print(d, k, i, queue)
    if k == 0:
        if len(queue) > 0:
            ans[i] = queue[0][1]
    elif k == 1:
        heappush(queue, (stx[i][1], stx[i][2]))
    else:
        heappop(queue)

print(*ans, sep='\n')
