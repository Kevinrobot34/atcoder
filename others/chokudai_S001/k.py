class BIT1():
    """
    Binary Indexed Tree (1-indexed)
    """
    def __init__(self, n):
        self.n = n
        self.bit = [0] * (self.n + 1)
        self.data = [0] * (self.n + 1)

    def add(self, idx, x):
        # add x to idx-th element
        # idx: 1-indexed
        self.data[idx] += x
        while idx <= self.n:
            self.bit[idx] += x
            idx += (idx & (-idx))

    def sum(self, idx):
        # get sum of [1, idx]
        # idx: 1-indexed
        s = 0
        while idx:
            s += self.bit[idx]
            idx -= (idx & (-idx))
        return s


MOD = 10**9 + 7
n = int(input())
a = list(map(int, input().split()))

fact = [1] * (n + 1)
for i in range(1, n):
    fact[i] = (fact[i - 1] * i) % MOD

bit = BIT1(n)
ans = 1
for i, ai in enumerate(a):
    rank = ai - bit.sum(ai - 1)
    ans += fact[n - 1 - i] * (rank - 1)
    ans %= MOD
    bit.add(ai, 1)
print(ans)
