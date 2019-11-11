import sys
input = sys.stdin.readline


class SegmentTree():
    """
    1-indexed Segment Tree
    """
    def __init__(self, n_, ele_id, operation_func):
        self.n = 1 << (n_ - 1).bit_length()
        self.data = [ele_id] * (2 * self.n)
        self.ele_id = ele_id
        self.operation_func = operation_func

    def __getitem__(self, idx):
        return self.data[idx + self.n]

    def build(self, data_init):
        for i in range(len(data_init)):
            self.data[i + self.n] = data_init[i]
        for i in range(self.n - 1, 0, -1):
            self.data[i] = self.operation_func(self.data[2 * i],
                                               self.data[2 * i + 1])

    def update(self, idx, x):
        # idx番目の要素をxに更新する
        idx += self.n
        self.data[idx] = x
        while idx > 0:
            idx //= 2
            self.data[idx] = self.operation_func(self.data[2 * idx],
                                                 self.data[2 * idx + 1])

    def query(self, l, r):
        l += self.n
        r += self.n
        ret = self.ele_id
        while l < r:
            if l % 2 == 1:  # right child
                ret = self.operation_func(ret, self.data[l])
                l += 1
            if r % 2 == 1:  # right child
                r -= 1
                ret = self.operation_func(ret, self.data[r])
            # go to parent-nodes
            l //= 2
            r //= 2
        return ret


n, q = map(int, input().split())

st_rmq = SegmentTree(n, (1 << 31) - 1, lambda a, b: min(a, b))
for _ in range(q):
    com, x, y = map(int, input().split())
    if com == 0:
        st_rmq.update(x, y)
    elif com == 1:
        ans = st_rmq.query(x, y + 1)
        print(ans)
