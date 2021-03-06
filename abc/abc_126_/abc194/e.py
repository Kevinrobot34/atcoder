class SegmentTree1():
    """
    1-indexed Segment Tree
    """
    def __init__(self, n_, ele_id, op_func):
        self.n = 1 << (n_ - 1).bit_length()  # size
        self.data = [ele_id] * (2 * self.n)  # binary tree (1-indexed)
        self.ele_id = ele_id  # identity element
        self.op_func = op_func  # binary operation of monoid

    def __getitem__(self, i):
        return self.data[i + self.n]

    def build(self, data_init):
        for i in range(len(data_init)):
            self.data[i + self.n] = data_init[i]  # set data in leaf
        for i in reversed(range(self.n)):
            self.data[i] = self.op_func(self.data[2 * i], self.data[2 * i + 1])

    def update(self, i, x):
        # change i-th element to x (i : 0-indexed)
        i += self.n
        self.data[i] = x
        while i > 1:
            i = i >> 1  # go to parenet-node
            self.data[i] = self.op_func(self.data[2 * i], self.data[2 * i + 1])

    def query(self, l, r):
        # query for interval [l, r) (l, r : 0-indexed)
        l += self.n
        r += self.n
        ret = self.ele_id
        while l < r:
            if l & 1:  # right child
                ret = self.op_func(ret, self.data[l])
                l += 1
            if r & 1:  # right child
                r -= 1
                ret = self.op_func(ret, self.data[r])
            # go to parent-nodes
            l = l >> 1
            r = r >> 1
        return ret


n, m = map(int, input().split())
a = list(map(int, input().split()))
INF = (1 << 31) - 1
st_rmq = SegmentTree1(n + 1, INF, lambda a, b: min(a, b))
st_rmq.build(list(range(n + 1)))
count = [0] * n
ans = INF
for i, ai in enumerate(a):
    if i >= m:
        count[a[i - m]] -= 1
        if count[a[i - m]] == 0:
            st_rmq.update(a[i - m], a[i - m])
    st_rmq.update(ai, INF)
    count[ai] += 1

    if i >= m - 1:
        # print(i, st_rmq.query(0, n + 1), sum(count))
        ans = min(ans, st_rmq.query(0, n + 1))

print(ans)
