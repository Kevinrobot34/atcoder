r, g, b, n = map(int, input().split())

ans = 0
for i in range(n // r + 1):
    for j in range(n // g + 1):
        m = r * i + g * j
        if m <= n and (n - m) % b == 0:
            ans += 1
        elif m > n:
            break

print(ans)
