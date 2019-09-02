from collections import defaultdict
import sys
input = sys.stdin.readline

n, h, w = map(int, input().split())
info = []
for i in range(n):
    r, c, a = map(int, input().split())
    info.append((r-1, c-1, a))

info.sort(key=lambda x: x[2], reverse=True)
print(info)

m = 0
ans = 0
dr = defaultdict(int)
dc = defaultdict(int)
while m < max(h + w, n):
    r, c, a = info[m]
    if dr[r] == 0 or dc[c] == 0:
        dr[r] += 1
        dc[c] += 1
        ans += a
        print(m, a)
    m += 1

print(ans)
