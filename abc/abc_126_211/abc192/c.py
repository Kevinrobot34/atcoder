n, k = map(int, input().split())
for _ in range(k):
    g1 = int(''.join(sorted(str(n), reverse=True)))
    g2 = int(''.join(sorted(str(n))))
    n = g1 - g2

print(n)
