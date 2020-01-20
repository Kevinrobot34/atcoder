n = int(input())
ans = n * 2
for x in range(1, n + 1):
    if x * x > n:
        break

    y = n // x
    ans = min(ans, abs(x - y) + (n - x * y))

print(ans)
