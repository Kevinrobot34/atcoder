import sys
input = sys.stdin.readline


def compress_coordinate(x: list, key=None, reverse=False):
    zipped = {}
    unzipped = {}
    for i, xi in enumerate(sorted(x, key=None, reverse=reverse)):
        zipped[xi] = i + 1
        unzipped[i + 1] = xi
    return zipped, unzipped


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


q = int(input())
query = []
coord = set()
for _ in range(q):
    s = input()
    if s[0] == '1':
        # update query
        _, a, b = map(int, s.split())
        coord.add(a)
        query.append((1, a, b))
    else:
        # evaluation query
        query.append((2, ))

zipped, unzipped = compress_coordinate(list(coord))
b_sum = 0
bit = BIT1(len(coord))
for i in range(q):
    if query[i][0] == 1:
        a = query[i][1]
        b = query[i][2]

        bit.add(zipped[a], 1)
        b_sum += b
    else:
        n = bit.sum(len(coord))
        idx1 = bit.bisect_left((n + 1) // 2)
        print(unzipped[idx1], b_sum)
