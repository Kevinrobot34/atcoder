import math
a, b = map(int, input().split())

ans = -1
for i in range(1, 1011):
    ai = math.floor(i * 1.08)
    bi = math.floor(i * 1.10)
    if ai == i + a and bi == i + b:
        ans = i
        break

print(ans)
