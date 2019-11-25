import sys
from operator import itemgetter
input = sys.stdin.readline


def compress_coordinate(x: list, key=None, reverse=False):
    zipped = {}
    unzipped = {}
    for i, xi in enumerate(sorted(set(x), key=None, reverse=reverse)):
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

    def add(self, idx, x):
        # add x to idx-th element
        # idx: 1-indexed
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


MOD = 998244353
n = int(input())
x_list = []
y_list = []
for i in range(n):
    x, y = map(int, input().split())
    x_list.append(x)
    y_list.append(y)
x_zipped, x_unzipped = compress_coordinate(x_list)
y_zipped, y_unzipped = compress_coordinate(y_list)

p = []
for i, (x, y) in enumerate(zip(x_list, y_list)):
    p.append((x_zipped[x], y_zipped[y], i))

info = [[0] * 5 for _ in range(n)]
p.sort(key=itemgetter(0))
# print(*p)
bit1 = BIT1(n)
for m, (px, py, idx) in enumerate(p):
    bit1.add(py, 1)
    s_left = bit1.sum(py) - 1
    s_right = (m + 1) - s_left - 1
    info[idx][2] = s_right
    info[idx][3] = s_left

p.sort(key=itemgetter(0), reverse=True)
# print(*p)

bit2 = BIT1(n)
for m, (px, py, idx) in enumerate(p):
    bit2.add(py, 1)
    s_left = bit2.sum(py) - 1
    s_right = (m + 1) - s_left - 1
    info[idx][1] = s_right
    info[idx][4] = s_left

ans = 0
for _, c1, c2, c3, c4 in info:
    c1 = pow(2, c1, MOD) - 1
    c2 = pow(2, c2, MOD) - 1
    c3 = pow(2, c3, MOD) - 1
    c4 = pow(2, c4, MOD) - 1
    ans += 1
    ans += c1 + c2 + c3 + c4
    ans += c1 * c3 * 2 + c2 * c4 * 2
    ans += c1 * c2 + c2 * c3 + c3 * c4 + c4 * c1
    ans += (c2 * c3 * c4 + c1 * c3 * c4 + c1 * c2 * c4 + c1 * c2 * c3) * 2
    ans += c1 * c2 * c3 * c4 * 2
    ans %= MOD

# print(*info, sep='\n')
print(ans)
