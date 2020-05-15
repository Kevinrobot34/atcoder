import math
p = float(input())

y = 2 * math.log(2) / 3
x = p * y
if x < 1.0:
    ans = p
else:
    t = math.log(x) / y
    ans = t + p * 2**(-t / 1.5)

print(ans)
