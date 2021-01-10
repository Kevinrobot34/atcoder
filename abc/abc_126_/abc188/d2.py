import sys
input = sys.stdin.readline

n, c = map(int, input().split())

event = []
for _ in range(n):
    ai, bi, ci = map(int, input().split())
    event.append((ai, ci))
    event.append((bi + 1, -ci))
event.sort()

d_cur = 0
p = 0
ans = 0
for d, v in event:
    ans += min(p, c) * (d - d_cur)
    p += v
    d_cur = d

print(ans)
