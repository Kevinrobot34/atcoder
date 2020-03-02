# checked : http://judge.u-aizu.ac.jp/onlinejudge/review.jsp?rid=4223494#1
import sys
input = sys.stdin.readline


class SegmentTree0():
    """
    0-indexed Segment Tree
    """
    def __init__(self, n_, ele_id, op_func):
        self.n = 1 << (n_ - 1).bit_length()  # size
        self.data = [ele_id] * (2 * self.n - 1)  # binary tree (0-indexed)
        self.ele_id = ele_id  # identity element
        self.op_func = op_func  # binary operation of monoid

    def __getitem__(self, i):
        return self.data[i + self.n - 1]

    def build(self, data_init):
        for i in range(len(data_init)):
            self.data[i + self.n - 1] = data_init[i]  # set data in leaf
        for i in range(self.n - 2, -1, -1):
            self.data[i] = self.op_func(self.data[2 * i + 1],
                                        self.data[2 * i + 2])

    def update(self, i, x):
        # change i-th element to x (i : 0-indexed)
        i += self.n - 1
        self.data[i] = x
        while i > 0:
            i = (i - 1) // 2  # go to parenet-node
            self.data[i] = self.op_func(self.data[2 * i + 1],
                                        self.data[2 * i + 2])

    def query(self, a, b):
        # query for interval [a, b) (a, b : 0-indexed)
        return self.query_(a, b, 0, 0, self.n)

    def query_(self, a, b, k, l, r):
        if r <= a or b <= l:
            # [a, b) and [l, r) have no intersection
            return self.ele_id
        if a <= l and r <= b:
            # [a, b) includes [l, r)
            return self.data[k]
        else:
            # [a, b) and [l, r) have some overlap
            child_l = self.query_(a, b, 2 * k + 1, l, (l + r) // 2)
            child_r = self.query_(a, b, 2 * k + 2, (l + r) // 2, r)
            return self.op_func(child_l, child_r)


n, q = map(int, input().split())
ele_id = (1 << 31) - 1
op_func = min
st_rmq = SegmentTree0(n, ele_id, op_func)
for _ in range(q):
    com, x, y = map(int, input().split())
    if com == 0:
        st_rmq.update(x, y)
    elif com == 1:
        ans = st_rmq.query(x, y + 1)
        print(ans)
