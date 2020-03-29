import sys
sys.setrecursionlimit(10**9)

MOD = 10**9 + 7
n = int(input())
g = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    a, b = map(int, input().split())
    g[a].append(b)
    g[b].append(a)

fact = [1] * (n + 1)  # i!
finv = [1] * (n + 1)  # (i!)^{-1}
iinv = [1] * (n + 1)  # i^{-1}
for i in range(2, n + 1):
    fact[i] = fact[i - 1] * i % MOD
    iinv[i] = MOD - iinv[MOD % i] * (MOD // i) % MOD
    finv[i] = finv[i - 1] * iinv[i] % MOD

print(fact)
print(finv)
print(iinv)

size1 = [1] * (n + 1)
dp1 = [1] * (n + 1)
dp2 = [1] * (n + 1)


def modinv(x, mod=MOD) -> int:
    return pow(x, mod - 2, mod)


def dfs1(v, vp):
    ans = 1
    for vn in g[v]:
        if vn == vp:
            continue
        dfs1(vn, v)
        ans *= dp1[vn] * finv[size1[vn]] % MOD
        ans %= MOD
        size1[v] += size1[vn]
    ans *= fact[size1[v] - 1]
    ans %= MOD

    dp1[v] = ans
    print('dfs1', v + 1, ans)


dfs1(1, 0)
print(dp1)
print(size1)


def dfs2(v, vp):
    m = size1[vp] - size1[v] - 1
    dp2[v] = dp2[vp] * fact[m] * finv[size1[vp] - 1] % MOD
    dp2[v] *= fact[size1[v]] * modinv(dp1[v]) % MOD
    dp2[v] %= MOD

    for vn in g[v]:
        if vp == vn:
            continue
        dfs2(vn, v)


dfs2(1, 0)
print(dp2)
