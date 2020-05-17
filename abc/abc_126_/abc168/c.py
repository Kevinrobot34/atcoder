import math
a, b, h, m = map(int, input().split())

t = h * 60 + m
th_a = (0.5 * t) % 360
th_b = (6.0 * t) % 360
th = min(abs(th_a - th_b), 360 - abs(th_a - th_b))
# print(th_a, th_b, th)
th = (th / 360) * (2 * math.pi)

c = math.sqrt(a**2 + b**2 - 2 * a * b * math.cos(th))
print(c)
