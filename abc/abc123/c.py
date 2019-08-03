import math
n = int(input())
a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())

f = min(a, b, c, d, e)
if n % f == 0:
    print(n // f - 1 + 5)
else:
    print(n // f + 5)
