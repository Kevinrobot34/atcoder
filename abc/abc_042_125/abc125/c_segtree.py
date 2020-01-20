from fractions import gcd
# def GCD(a: int, b: int) -> int:
#     return a if b == 0 else GCD(b, a % b)


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

    def init(self, data_init):
        for i in range(len(data_init)):
            self.data[i + self.n - 1] = data_init[i]
        for i in range(self.n - 2, -1, -1):
            self.data[i] = self.operation_func(self.data[2 * i + 1],
                                               self.data[2 * i + 2])

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


n = int(input())
a = list(map(int, input().split()))
seg_gcd = SegTree(n, 0, gcd)
seg_gcd.init(a)

ans = seg_gcd.data[0]
for i in range(n):
    # seg_gcd.update(i, 0)
    # ans = max(ans, seg_gcd.data[0])
    # seg_gcd.update(i, a[i])
    ans = max(ans, gcd(seg_gcd.query(0, i), seg_gcd.query(i + 1, n)))

print(ans)
