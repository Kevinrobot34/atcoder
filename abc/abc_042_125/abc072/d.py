import math
n = int(input())
p = list(map(int, input().split()))

x = 0
ans = 0
for i in range(n):
    if i + 1 == p[i]:
        x += 1
    else:
        ans += math.ceil(x / 2)
        x = 0
ans += math.ceil(x / 2)

print(ans)
