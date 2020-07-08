n = int(input())
a = b = c = 0
for _ in range(n):
    n, m, l = sorted(map(int, input().split()))
    a = max(a, n)
    b = max(b, m)
    c = max(c, l)
ans = a * b * c
print(ans)
