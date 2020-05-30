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

    if m == 1 and v == 1:
        ans_i = 1 * pow(n - 1, n_minus)
    else:
        ans_i = 0
        for i in range(v + 1):
            ans_i += ((m - 1 + i) * comb(v, i) * pow(n - m, i, MOD) %
                      MOD) * pow(m - 1, v - i, MOD) % MOD
            ans_i %= MOD
        print(ans_i)
        ans_i *= pow(n - 1, n_minus - v)
        ans_i %= MOD

    ans += ans_i
    print('k v m ans_i', k, v, m, ans_i)
    ans %= MOD
print(ans)
