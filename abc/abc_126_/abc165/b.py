import math
x = int(input())

c = 100
ans = 0
while c < x:
    c = math.floor(c * 1.01)
    ans += 1

print(ans)
