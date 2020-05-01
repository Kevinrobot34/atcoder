def comb(n: int, k: int) -> int:
    if n < k or n < 0 or k < 0:
        return 0
    k = min(k, n - k)
    ans = 1
    for i in range(1, k + 1):
        ans *= n - i + 1
        ans //= i
    return ans


n, d = map(int, input().split())
x, y = map(int, input().split())

if x % d == 0 and y % d == 0:
    x //= d
    y //= d
    ans = 0.0

    for nx in range(n + 1):
        ny = n - nx
        if (nx + x) % 2 != 0:
            continue
        if (ny + y) % 2 != 0:
            continue

        if x > nx:
            continue
        if y > ny:
            continue
        nx_p = (nx + x) // 2
        ny_p = (ny + y) // 2
        # print(n, nx, nx_p, ny, ny_p)
        tmp = comb(n, nx) / (4**n)
        tmp *= comb(nx, nx_p)
        tmp *= comb(ny, ny_p)
        ans += tmp
else:
    ans = 0.0

print(ans)
