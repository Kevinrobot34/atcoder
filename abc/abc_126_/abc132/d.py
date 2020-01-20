MOD = 10**9 + 7
MAX = 2000 + 5
fact = [1 for _ in range(MAX)]
finv = [1 for _ in range(MAX)]
for i in range(2, MAX):
    fact[i] = fact[i - 1] * i % MOD
    finv[i] = pow(fact[i], MOD-2, MOD)

def comb(n, k):
    if n < k or n < 0 or k < 0:
        return 0
    return (fact[n] * finv[k] % MOD) * finv[n-k] % MOD

n, k = map(int, input().split())

for i in range(1, k+1):
    ans = comb(k-1, i-1) * comb(n-k+1, i) % MOD
    print(ans)
