MOD = 10**9 + 7
n = int(input())
a = list(map(int, input().split()))


def comb(n: int, k: int, MOD: int) -> int:
    if n < k or n < 0 or k < 0:
        return 0
    k = min(k, n - k)
    if k == 0:
        return 1
    iinv = [1] * (k + 1)
    ans = n
    for i in range(2, k + 1):
        iinv[i] = MOD - iinv[MOD % i] * (MOD // i) % MOD
        ans *= (n + 1 - i) * iinv[i] % MOD
        ans %= MOD
    return ans


ans = 1
x = a[0]
cnt = 0
for i in range(1, n):
    if a[i] == -1:
        cnt += 1
        continue

    if cnt > 0:
        ans *= comb(cnt + a[i] - x, cnt, MOD)
        ans %= MOD
        cnt = 0

    x = a[i]

print(ans)
