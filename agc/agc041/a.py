n, a, b = map(int, input().split())

if (b - a) % 2 == 0:
    ans = (b - a) // 2
else:
    ans = min(a - 1, n - b) + 1 + (b - a - 1) // 2

print(ans)
