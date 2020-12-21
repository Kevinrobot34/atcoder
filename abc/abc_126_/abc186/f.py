from operator import itemgetter
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


h, w, m = map(int, input().split())
xy = [tuple(map(int, input().split())) for _ in range(m)]
ans = 0

y_min = w
x_min = h
for xi, yi in xy:
    if xi == 1:
        y_min = min(y_min, yi)
    if yi == 1:
        x_min = min(x_min, xi)

for yi in range(y_min + 1, w + 1):
    xy.append((1, yi))
    m += 1
for xi in range(x_min + 1, h + 1):
    xy.append((xi, 1))
    m += 1

bit = BIT1(w + 1)
xy.sort(key=lambda a: (a[0], -a[1]))
x0 = y0 = -1
for i, (xi, yi) in enumerate(xy):
    if x0 != xi:
        cnt = bit.sum(w) - bit.sum(yi)
        ans += cnt
    else:
        cnt = bit.sum(y0 - 1) - bit.sum(yi)
        ans += cnt
    if bit.data[yi] == 0:
        bit.add(yi, 1)
    x0, y0 = xi, yi

print(h * w - m - ans)
