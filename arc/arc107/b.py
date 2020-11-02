n, k = map(int, input().split())


def func(m):
    if m <= n + 1:
        return m - 1
    else:
        return 2 * n + 1 - m


ans = 0
for y in range(2, 2 * n + 1):
    x = y + k
    if x < 2 or x > 2 * n:
        continue
    ans += func(x) * func(y)

print(ans)
