class BIT1():
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
        # return minimum idx where bit.sum(idx) >= w
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
        # return minimum idx where bit.sum(idx) > w
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


n = int(input())
p = list(map(int, input().split()))

p2idx = [0] * (n + 1)
for i in range(1, n + 1):
    p2idx[p[i - 1]] = i

ans = 0
bit = BIT1(n)
for x in reversed(range(1, n + 1)):
    idx = p2idx[x]
    bit.add(idx, 1)
    idx_rank = bit.sum(idx)
    idx_l2 = bit.bisect_left(idx_rank - 2)
    idx_l1 = bit.bisect_left(idx_rank - 1)
    idx_r1 = bit.bisect_left(idx_rank + 1)
    idx_r2 = bit.bisect_left(idx_rank + 2)

    cnt = 0
    cnt += (idx_l1 - idx_l2) * (idx_r1 - idx)
    cnt += (idx - idx_l1) * (idx_r2 - idx_r1)
    ans += x * cnt

print(ans)
