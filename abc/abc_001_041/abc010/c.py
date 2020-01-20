import math
xa, ya, xb, yb, t, v = map(int, input().split())
n = int(input())

ans = "NO"
for i in range(n):
    x, y = map(int, input().split())
    d1 = math.sqrt((x - xa)**2 + (y - ya)**2)
    d2 = math.sqrt((x - xb)**2 + (y - yb)**2)
    if d1 + d2 <= t * v:
        ans = "YES"

print(ans)
