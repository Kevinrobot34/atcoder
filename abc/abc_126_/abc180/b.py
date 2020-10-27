import math
n = int(input())
x = list(map(int, input().split()))

d1 = sum(abs(xi) for xi in x)
d2 = math.sqrt(sum(xi**2 for xi in x))
d3 = max(abs(xi) for xi in x)

print(d1)
print(d2)
print(d3)
