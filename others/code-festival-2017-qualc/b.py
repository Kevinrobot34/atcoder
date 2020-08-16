from itertools import product
n = int(input())
a = list(map(int, input().split()))

ans = 0
for x in product([-1, 0, 1], repeat=n):
    b = [ai + xi for ai, xi in zip(a, x)]
    if any(bi % 2 == 0 for bi in b):
        ans += 1

print(ans)
