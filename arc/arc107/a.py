def f(n):
    return n * (n + 1) // 2


MOD = 998244353
a, b, c = map(int, input().split())
ans = f(a) * f(b) * f(c) % MOD
print(ans)
