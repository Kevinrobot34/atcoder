import math
a, b, x = map(int, input().split())

if x <= a * a * b / 2:
    c = 2 * x / (a * b)
    ans = math.atan2(b, c)
    ans *= 360 / (2 * math.pi)
else:
    c = 2 * b - 2 * x / (a**2)
    ans = math.atan2(c, a)
    ans *= 360 / (2 * math.pi)

print(ans)
