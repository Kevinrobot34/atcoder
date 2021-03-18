import sys
sys.setrecursionlimit(10**8)
INF = float('inf')


def ext_gcd(a, b):
    if b:
        g, y, x = ext_gcd(b, a % b)
        y -= (a // b) * x
        return g, x, y
    return a, 1, 0


def crt(m1, m2, b1, b2):
    g, p, q = ext_gcd(m1, m2)
    if (b2 - b1) % g != 0:
        return 0, -1
    m = m1 * m2 // g
    s = (b2 - b1) // g
    r = b1 + s * m1 * p
    r %= m
    return r, m


def solve(x, y, p, q):
    m1 = 2 * (x + y)
    m2 = p + q
    ret = INF

    for i in range(y):
        for j in range(q):
            r, m = crt(m1, m2, x + i, p + j)
            if (r, m) != (0, -1):
                # print(i, j, r, m)
                ret = min(ret, r)

    return 'infinity' if ret == INF else ret


t = int(input())
for _ in range(t):
    x, y, p, q = map(int, input().split())
    ans = solve(x, y, p, q)
    print(ans)
