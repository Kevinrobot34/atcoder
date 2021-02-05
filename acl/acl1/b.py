def get_divisor(n):
    divisor = []
    for i in range(1, n + 1):
        if i * i > n:
            break
        if n % i == 0:
            yield i
            if n // i != i:
                yield n // i


# return (g, x, y) which satisfies ax + by = g and g = GCD(a,b)
def ext_gcd(a, b):
    if b != 0:
        g, y, x = ext_gcd(b, a % b)
        y -= (a // b) * x
        return g, x, y
    return a, 1, 0


# return (r, m) which satisfies x \equiv r (mod m) as solution
# when no solution ( (b1-b2) % gcd(m1, m2) != 0 ), return(0, -1)
def crt(m1, m2, b1, b2):
    g, p, _ = ext_gcd(m1, m2)
    if (b2 - b1) % g != 0:
        return 0, -1
    m = m1 * (m2 // g)
    s = (b2 - b1) // g
    r = b1 + (s * m1 % m) * p
    r %= m
    return r, m


n = int(input())
ans = n
for x in get_divisor(2 * n):
    y = 2 * n // x
    r, m = crt(x, y, 0, y - 1)
    # print(x, y, r, m)
    if r > 0:
        ans = min(ans, r)
print(ans)
