import sys
input = sys.stdin.readline


class SegTree():
    def __init__(self, n_, ele_id, operation_func):
        self.n = 1
        while self.n < n_:
            self.n *= 2
        self.data = [ele_id] * (2 * self.n - 1)
        self.ele_id = ele_id
        self.operation_func = operation_func

    def __getitem__(self, idx):
        return self.data[idx + self.n - 1]

    def update(self, idx, x):
        # idx番目の要素をxに更新する
        idx += self.n - 1
        self.data[idx] = x
        while idx > 0:
            idx = (idx - 1) // 2
            self.data[idx] = self.operation_func(self.data[2 * idx + 1],
                                                 self.data[2 * idx + 2])

    def query(self, a, b):
        return self.query_(a, b, 0, 0, self.n)

    def query_(self, a, b, k, l, r):
        # [a, b)の最小値を求める
        if r <= a or b <= l:
            # [a, b)が[l, r)と交差しない
            return self.ele_id

        if a <= l and r <= b:
            # [a, b)が[l, r)を完全に含む
            return self.data[k]
        else:
            # [a, b)と[l, r)は一部被る
            child_l = self.query_(a, b, 2 * k + 1, l, (l + r) // 2)
            child_r = self.query_(a, b, 2 * k + 2, (l + r) // 2, r)
            return self.operation_func(child_l, child_r)


n, q = map(int, input().split())

st_rsq = SegTree(n, 0, lambda a, b: a + b)
for _ in range(q):
    com, x, y = map(int, input().split())
    if com == 0:
        x -= 1
        st_rsq.update(x, st_rsq[x] + y)
    elif com == 1:
        x -= 1
        y -= 1
        ans = st_rsq.query(x, y + 1)
        print(ans)
