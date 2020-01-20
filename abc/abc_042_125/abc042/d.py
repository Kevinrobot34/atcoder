h, w, a, b = map(int, input().split())

MOD = 10**9 + 7
MAX = h+w + 5
fact = [1 for _ in range(MAX)]
finv = [1 for _ in range(MAX)]
for i in range(2, MAX):
    fact[i] = fact[i - 1] * i % MOD
    finv[i] = pow(fact[i], MOD-2, MOD)

def comb(n: int, k: int) -> int:
    if n < k or n < 0 or k < 0:
        return 0
    return (fact[n] * finv[k] % MOD) * finv[n-k] % MOD

def path(x, y):
    return comb(x+y-2, x-1)

ans = 0
for j in range(b+1, w+1):
    # print((h-a, j), (a, w-j+1))
    ans += (path(h-a, j) * path(a, w-j+1)) % MOD
    ans %= MOD
print(ans)
