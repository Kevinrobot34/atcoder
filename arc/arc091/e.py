n, a, b = map(int, input().split())

if a > n or b > n or a + b > n + 1:
    print(-1)
else:
    ans = []
    ans += list(range(n - a + 1, n + 1))
    ans += list(reversed(range(1, b)))
    tmp = list(range(b, n - a + 1))
    if len(tmp) > 0:
        ans += tmp[1::2] + tmp[::2]
    print(*ans)
