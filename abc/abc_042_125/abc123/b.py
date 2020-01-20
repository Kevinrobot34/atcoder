import math
a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())

a, b, c, d, e = sorted((a, b, c, d, e), key=lambda x: x%10 if x%10>0 else 10, reverse=True)

ans = int(math.ceil(a / 10))*10 \
        + int(math.ceil(b / 10))*10 \
        + int(math.ceil(c / 10))*10 \
        + int(math.ceil(d / 10))*10 \
        + e
print(ans)
