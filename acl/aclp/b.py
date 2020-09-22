import sys
input = sys.stdin.readline


class BIT1():
    """
    Binary Indexed Tree (1-indexed)
    """
    def __init__(self, n, data=None):
        self.n = n
        self.bit = [0] * (self.n + 1)
        self.data = [0] * (self.n + 1)
        if data:
            self.build(data)

    def build(self, data):
        for i in range(self.n):
            self.bit[i + 1] = self.data[i + 1] = data[i]
        for i in range(1, self.n):
            j = i + (i & (-i))
            if j <= self.n:
                self.bit[j] += self.bit[i]

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


n, q = map(int, input().split())
a = list(map(int, input().split()))
bit = BIT1(n, a)
for _ in range(q):
    t, p, q = map(int, input().split())
    if t == 0:
        bit.add(p + 1, q)
    else:
        print(bit.sum(q) - bit.sum(p))
