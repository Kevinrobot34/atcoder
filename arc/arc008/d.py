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


class SegmentTree1():
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
        # idx(0-indexed)番目の要素をxに更新する
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
segtree = SegmentTree1(len(pp), ele_id, op)

ans_min = ans_max = 1
for p, a, b in query:
    p_idx = p_zipped[p]  # 座標圧縮
    segtree.update(p_idx, (a, b))

    # a_whole, b_whole = segtree.query(0, n)
    a_whole, b_whole = segtree.data[1]
    cand = a_whole * 1 + b_whole
    ans_min = min(ans_min, cand)
    ans_max = max(ans_max, cand)

print(ans_min)
print(ans_max)
