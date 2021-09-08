import math

r, x, y = map(int, input().split())
if x**2 + y**2 < r**2:
    ans = 2
else:
    ans = math.ceil(math.sqrt(x**2 + y**2) / r)
print(ans)
