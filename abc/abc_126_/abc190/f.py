class BIT1():
    """
    Binary Indexed Tree (1-indexed)
    """
    def __init__(self, n):
        self.n = n
        self.bit = [0] * (self.n + 1)
        self.data = [0] * (self.n + 1)

    def add(self, idx, x):
        # add x to idx(>0)-th element
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


n = int(input())
a = list(map(lambda x: int(x) + 1, input().split()))
bit = BIT1(n)
ans = [0] * n
for i, ai in enumerate(a):
    ans[0] += i - bit.sum(ai)
    bit.add(ai, 1)
for k in range(1, n):
    ans[k] = ans[k - 1] - (a[k - 1] - 1) + (n - a[k - 1])
print(*ans, sep='\n')
