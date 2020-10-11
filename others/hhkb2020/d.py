MOD = 10**9 + 7


def func(n, a, b):
    x1 = (n - a + 1)**2 * (n - b + 1)**2 % MOD
    x2 = (n - a + 1) * (n - b + 1) % MOD
    if n < a + b:
        x3 = 0
    else:
        x3 = (n - a - b + 2) * (n - a - b + 1) % MOD

    x = x1 - ((x2 - x3) % MOD)**2 % MOD
    x %= MOD
    return x


t = int(input())
for _ in range(t):
    n, a, b = map(int, input().split())
    ans = func(n, a, b)
    print(ans)
