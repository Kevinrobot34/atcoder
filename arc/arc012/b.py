n, va, vb, l = map(int, input().split())

for _ in range(n):
    l = (l / va) * vb

print(l)
