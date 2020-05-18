import cmath
a, b, h, m = map(int, input().split())

t = h * 60 + m
th_a = ((0.5 * t) / 360.0) * 2 * cmath.pi
th_b = ((6.0 * t) / 360.0) * 2 * cmath.pi

za = cmath.rect(a, th_a)
zb = cmath.rect(b, th_b)

c = abs(za - zb)
print(c)
