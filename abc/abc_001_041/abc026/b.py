import math

n = int(input())
r = [int(input()) for _ in range(n)]
r.sort(reverse=True)

ans = 0.0
for i, ri in enumerate(r):
    ans += math.pi * ri * ri * ((-1)**i)

print(ans)
