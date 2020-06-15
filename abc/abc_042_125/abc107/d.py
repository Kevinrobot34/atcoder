n = int(input())
a = list(map(int, input().split()))
m = (n * (n + 1) // 2) // 2 + 1


class BIT1():
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


def check(x):
    # MofM が x以下である
    # x以下の要素が (n*(n+1)//2)//2 + 1 個以上ある

    s = 0
    c = [0] * (n + 1)
    for i in range(n):
        c[i + 1] = c[i]
        if a[i] <= x:
            c[i + 1] += 1
    d = [2 * c[i] - i + n + 1 for i in range(n + 1)]
    d_max = max(d)
    bit = BIT1(d_max)

    cnt = 0
    for i in range(n + 1):
        cnt += bit.sum(d[i] - 1)
        bit.add(d[i], 1)
    return cnt >= m


lb = 0  # False
ub = max(a) + 1  # True
while ub - lb > 1:
    mid = (ub + lb) // 2
    if check(mid):
        ub = mid
    else:
        lb = mid

print(ub)
