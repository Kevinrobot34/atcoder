from bisect import bisect_left, bisect_right
from collections import deque
import sys
input = sys.stdin.readline
n = int(input())
a = [int(input()) for _ in range(n)]

dq = deque([a[0]])
for i in range(1, n):
    idx = bisect_left(dq, a[i])
    if idx == 0:
        dq.appendleft(a[i])
    else:
        dq[idx-1] = a[i]

print(len(dq))
