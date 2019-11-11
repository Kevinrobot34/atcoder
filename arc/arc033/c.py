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
        self.data[idx] += x
        while idx > 0:
            idx = idx >> 1
            self.data[idx] = self.operation_func(self.data[2 * idx],
                                                 self.data[2 * idx + 1])

    def query(self, l, r):
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


q = int(input())
X_MAX = 2 * 10**5 + 1
seg_rsq = SegmentTree(X_MAX, 0, lambda a, b: a + b)
for _ in range(q):
    t, x = map(int, input().split())
    if t == 1:
        seg_rsq.update(x, 1)
    else:
        lb = 0  # False
        ub = X_MAX  # True
        while ub - lb > 1:
            mid = (ub + lb) // 2
            if seg_rsq.query(0, mid) < x:
                lb = mid
            else:
                ub = mid

        print(ub - 1)
        seg_rsq.update(ub - 1, -1)
