import sys
input = sys.stdin.readline


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


n, k = map(int, input().split())
a = [int(input()) for _ in range(n)]
s = [0] * (n + 1)
for i in range(n):
    s[i + 1] = s[i] + a[i]
t = [s[i] - k * i for i in range(n + 1)]

# 座標圧縮
zipped = {}
for i, xi in enumerate(sorted(set(t))):
    zipped[xi] = i + 1
m = len(zipped)
t2 = [0] * (n + 1)
for i in range(n + 1):
    t2[i] = zipped[t[i]]

ans = 0
bit = BIT1(m)
for i in range(n + 1):
    ans += bit.sum(t2[i])
    bit.add(t2[i], 1)
print(ans)
