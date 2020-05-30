from collections import defaultdict
import sys
sys.setrecursionlimit(10**9)


class UnionFind():
    def __init__(self, n):
        self.par = [-1] * n

    def root(self, x):
        if self.par[x] < 0:
            return x
        else:
            self.par[x] = self.root(self.par[x])  # contraction
            return self.par[x]

    def unite(self, x, y):
        x, y = self.root(x), self.root(y)
        if x != y:
            if self.par[x] > self.par[y]:  # merge technique
                x, y = y, x
            self.par[x] += self.par[y]
            self.par[y] = x

    def same(self, x, y):
        return self.root(x) == self.root(y)

    def size(self, x):
        return -self.par[self.root(x)]


MOD = 10**9 + 7

MAX = 5000 + 5
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


n = int(input())
p = list(map(lambda x: int(x), input().split()))
for i in range(n):
    if p[i] != -1:
        p[i] -= 1

n_minus = 0
uf = UnionFind(n)
for i, pi in enumerate(p):
    if pi == -1:
        n_minus += 1
        continue

    uf.unite(i, pi)

group = defaultdict(int)
for i, pi in enumerate(p):
    if pi == -1:
        group[uf.root(i)] += 1
    else:
        group[uf.root(i)] += 0

print('n_minus', n_minus)
print(group)

ans = 0
for k, v in group.items():
    m = uf.size(k)
    ans += (m - 1) * pow(n - 1, n_minus, MOD)
    ans %= MOD

print(ans)

ans2 = 0
for k1, v1 in group.items():
    m1 = uf.size(k1)
    for k2, v2 in group.items():
        if k1 == k2:
            continue
        m2 = uf.size(k2)

        ans_i = pow(n - 1, v1 + v2, MOD)
        z = pow(n - 1 - m1, v2, MOD) * pow(n - 1 - m2, v1, MOD) % MOD
        ans_i = (MOD + ans_i - z) % MOD
        ans_i *= pow(n - 1, n_minus - v1 - v2, MOD)

        ans2 += ans_i
ans2 //= 2

ans += ans2
print(ans)
