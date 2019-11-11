class BIT0():
    """
    Binary Indexed Tree (0-indexed)
    """
    def __init__(self, n):
        self.n = n
        self.bit = [0] * (self.n)
        self.data = [0] * (self.n)

    def build(self, data):
        pass

    def add(self, idx, x):
        # add x to idx-th element
        # idx: 0-indexed
        self.data[idx] += x
        while idx < self.n:
            self.bit[idx] += x
            idx = idx | (idx + 1)

    def sum(self, idx):
        # get sum of [0, idx)  (`idx` elements)
        # idx: 0-indexed
        s = 0
        idx -= 1
        while idx >= 0:
            s += self.bit[idx]
            idx = (idx & (idx + 1)) - 1
        return s

    def bisect_left(self, w):
        # condition : always all element is not minus
        # return minimum idx where sum(idx) >= w
        if w < 0:
            return 0
        idx = -1  # self.bit[idx] < w
        k = 1 << ((self.n).bit_length() - 1)
        while k > 0:
            if idx + k < self.n and self.bit[idx + k] < w:
                w -= self.bit[idx + k]
                idx += k
            k = k >> 1
        return idx + 1

    def bisect_right(self, w):
        # condition : always all element is not minus
        # return minimum idx where sum(idx) > w
        if w < 0:
            return 0
        idx = -1  # self.bit[idx] <= w
        k = 1 << ((self.n).bit_length() - 1)
        while k > 0:
            if idx + k < self.n and self.bit[idx + k] <= w:
                w -= self.bit[idx + k]
                idx += k
            k = k >> 1
        return idx + 1


n = 10
bit0 = BIT0(n)

bit0.add(0, 1)
bit0.add(3, 2)
bit0.add(7, 1)

cs = []
for i in range(1, n + 1):
    cs.append(bit0.sum(i))
list(range(10))
cs

for x in range(6):
    print(x, bit0.bisect_left(x), bit0.bisect_right(x))
