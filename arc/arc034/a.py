n = int(input())
p = []
for _ in range(n):
    a, b, c, d, e = map(int, input().split())
    x = a + b + c + d + e * 110 / 900
    p.append(x)

ans = max(p)
print(ans)
