MOD = 10 ** 9 + 7
MAX = 200000 + 5
fact = [1 for _ in range(MAX)]
finv = [1 for _ in range(MAX)]
for i in range(2, MAX):
    fact[i] = fact[i - 1] * i % MOD
    finv[i] = pow(fact[i], MOD-2, MOD)

def comb(n: int, k: int) -> int:
    if n < k or n < 0 or k < 0:
        return 0
    return (fact[n] * finv[k] % MOD) * finv[n-k] % MOD

n, m, k = map(int, input().split())

ans = 0
for i in range(n):
    for j in range(m):
        a = j * (j+1) // 2
        b = (m-1-j) * (m-1-j+1) // 2
        ans += (a + b) * i + m * (i*(i+1)//2) + a
        ans %= MOD

ans *= comb(n*m-2, k-2)
ans %= MOD

print(ans)
