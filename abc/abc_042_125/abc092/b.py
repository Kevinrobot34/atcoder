import math
n = int(input())
d, x = map(int, input().split())

ans = x
for i in range(n):
    a = int(input())
    ans += math.ceil(d / a)
print(ans)
