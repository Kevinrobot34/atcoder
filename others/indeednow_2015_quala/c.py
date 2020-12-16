from bisect import bisect_left, bisect_right
import sys
input = sys.stdin.readline

n = int(input())
s = [int(input()) for _ in range(n)]
t = [si for si in s if si > 0]
t.sort(reverse=True)

q = int(input())
for _ in range(q):
    ki = int(input())

    if ki < len(t):
        ans = t[ki] + 1
    else:
        ans = 0
    print(ans)
