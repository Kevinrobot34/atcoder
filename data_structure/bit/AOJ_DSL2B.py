class BIT():
    """
    Binary Indexed Tree (1-indexed)
    """
    def __init__(self, n):
        self.n = n
        self.bit = [0] * (self.n + 1)
        self.data = [0] * (self.n + 1)

    def build(self, data):
        pass

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

    def bisect_left(self, w):
        # condition : always all element is not minus
        # return minimum idx where sum(idx) >= w
        if w <= 0:
            return 0
        idx = 0  # self.bit[idx] < w
        k = 1 << ((self.n).bit_length() - 1)
        while k > 0:
            if idx + k <= self.n and self.bit[idx + k] < w:
                w -= self.bit[idx + k]
                idx += k
            k = k >> 1
        return idx + 1

    def bisect_right(self, w):
        # condition : always all element is not minus
        # return minimum idx where sum(idx) > w
        if w < 0:
            return 0
        idx = 0  # self.bit[idx] <= w
        k = 1 << ((self.n).bit_length() - 1)
        while k > 0:
            if idx + k <= self.n and self.bit[idx + k] <= w:
                w -= self.bit[idx + k]
                idx += k
            k = k >> 1
        return idx + 1


n, q = map(int, input().split())

bit = BIT(n)
for _ in range(q):
    com, x, y = map(int, input().split())
    if com == 0:
        bit.add(x, y)
    elif com == 1:
        ans = bit.sum(y) - bit.sum(x - 1)
        print(ans)
