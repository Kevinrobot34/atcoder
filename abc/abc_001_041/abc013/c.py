n, h = map(int, input().split())
a, b, c, d, e = map(int, input().split())

ans = min(a, c) * n
for q in range(n + 1):
    p_tmp = (n * e - h - q * (d + e)) // (b + e) + 1
    if p_tmp > n - q:
        continue

    p = max(0, p_tmp)
    ans = min(ans, p * a + q * c)

print(ans)
