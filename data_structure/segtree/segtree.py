import sys
input = sys.stdin.readline


class SegTree():
    def __init__(self, n_, ele_id, update_func, operation_func):
        self.n = 1
        while self.n < n_:
            self.n *= 2
        self.data = [ele_id] * (2 * self.n - 1)
        self.ele_id = ele_id
        self.update_func = update_func
        self.operation_func = operation_func

    def update(self, idx, x):
        idx += self.n - 1
        self.data[idx] = self.update_func(self.data[idx], x)
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

st = SegTree(n, (1 << 31) - 1, lambda data, x: x, lambda a, b: min(a, b))
for _ in range(q):
    com, x, y = map(int, input().split())
    if com == 0:
        st.update(x, y)
    elif com == 1:
        ans = st.query(x, y + 1)
        print(ans)
