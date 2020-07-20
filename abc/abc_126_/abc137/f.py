p = int(input())
a = list(map(int, input().split()))

MOD = p
MAX = p + 10
fact = [1] * (MAX + 1)  # i!
finv = [1] * (MAX + 1)  # (i!)^{-1}
iinv = [1] * (MAX + 1)  # i^{-1}
for i in range(2, MAX + 1):
    fact[i] = fact[i - 1] * i % MOD
    iinv[i] = MOD - iinv[MOD % i] * (MOD // i) % MOD
    finv[i] = finv[i - 1] * iinv[i] % MOD


def comb(n: int, k: int) -> int:
    if n < k or n < 0 or k < 0:
        return 0
    return (fact[n] * finv[k] % MOD) * finv[n - k] % MOD


b = [0] * p
for j in range(p):
    if a[j] == 1:
        # (1 - (x-j)**(p-1)) の係数を足す
        b[0] += 1
        for k in range(p):
            b[k] += comb(p - 1, k) * pow(j, p - 1 - k, p) * (-1)**((p - k) % 2)
            b[k] %= p

print(*b)
