import sys
sys.setrecursionlimit(10**9)


class SegmentTree1():
    """
    1-indexed Segment Tree
    """
    def __init__(self, n_, ele_id, operation_func):
        self.n = 1 << (n_ - 1).bit_length()  # size
        self.data = [ele_id] * (2 * self.n)  # binary tree
        self.ele_id = ele_id  # identity element
        self.operation_func = operation_func  # binary operation of monoid

    def __getitem__(self, idx):
        return self.data[idx + self.n]

    def build(self, data_init):
        for i in range(len(data_init)):
            self.data[i + self.n] = data_init[i]
        for i in range(self.n - 1, 0, -1):
            self.data[i] = self.operation_func(self.data[2 * i],
                                               self.data[2 * i + 1])

    def update(self, idx, x):
        # change idx-th element to x (idx : 0-indexed)
        idx += self.n
        self.data[idx] = x
        while idx > 1:
            idx = idx >> 1
            self.data[idx] = self.operation_func(self.data[2 * idx],
                                                 self.data[2 * idx + 1])

    def query(self, l, r):
        # query for interval [l, r) (l, r : 0-indexed)
        l += self.n
        r += self.n
        ret = self.ele_id
        while l < r:
            if l & 1:  # right child
                ret = self.operation_func(ret, self.data[l])
                l += 1
            if r & 1:  # right child
                r -= 1
                ret = self.operation_func(ret, self.data[r])
            # go to parent-nodes
            l = l >> 1
            r = r >> 1
        return ret


n, m = map(int, input().split())
s = input()

dp = [-1] * (n + 1)
dp[n] = 1
roulette = [0] * (n + 1)

INF = 10**10
INF_PAIR = (INF, -1)
operation_func = lambda a, b: a if a[0] < b[0] else (b if a[0] > b[0] else
                                                     (a if a[1] < b[1] else b))
rmq = SegmentTree1(n + 1, INF_PAIR, operation_func)
rmq.update(n, (0, n))
for i in range(n - 1, -1, -1):
    if s[i] == '1':
        continue
    val, idx = rmq.query(i + 1, min(n, i + m) + 1)
    if val != INF:
        roulette[i] = idx - i
        dp[i] = val + 1
        rmq.update(i, (val + 1, i))

if dp[0] == -1:
    print(-1)
else:
    ans = []
    idx = 0
    while idx < n:
        ans.append(roulette[idx])
        idx += roulette[idx]
    print(*ans)
