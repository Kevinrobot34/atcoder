import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)


def compress_coordinate(x: list, key=None, reverse=False):
    zipped = {}
    unzipped = {}
    for i, xi in enumerate(sorted(set(x), key=None, reverse=reverse)):
        zipped[xi] = i
        unzipped[i] = xi
    return zipped, unzipped


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


n, m = map(int, input().split())
query = []
pp = []
for i in range(m):
    p, a, b = map(float, input().split())
    p = int(p) - 1
    query.append((p, a, b))
    pp.append(p)

# 座標圧縮
p_zipped, _ = compress_coordinate(pp)


# 順序に注意
# op(a, b)(x) = fb(fa(x))
# op = lambda ta, tb: (ta[0] * tb[0], tb[0] * ta[1] + tb[1])
def op(fx, gx):
    a, b = fx
    c, d = gx
    # c*(ax+b) + d
    return (a * c, b * c + d)


ele_id = (1.0, 0.0)
segtree = SegTree(len(pp), ele_id, op)

ans_min = ans_max = 1
for p, a, b in query:
    p_idx = p_zipped[p]  # 座標圧縮
    segtree.update(p_idx, (a, b))

    # a_whole, b_whole = segtree.query(0, n)
    a_whole, b_whole = segtree.data[0]
    cand = a_whole * 1 + b_whole
    ans_min = min(ans_min, cand)
    ans_max = max(ans_max, cand)

print(ans_min)
print(ans_max)
