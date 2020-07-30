a, b, k = map(int, input().split())

for i in range(k):
    if i % 2 == 0:
        b += a // 2
        a //= 2
    else:
        a += b // 2
        b //= 2

print(a, b)
