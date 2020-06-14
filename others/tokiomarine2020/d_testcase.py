import random
n = 2**18 - 1

print(n)
for _ in range(n):
    v = random.randrange(1, 10**5 + 1)
    w = random.randrange(1, 10**5 + 1)
    print(v, w)

q = 10**5
print(q)
for _ in range(n):
    v = random.randrange(n // 2, n + 1)
    l = 10**5
    print(v, l)
