import sys
input = sys.stdin.readline
INF = 1 << 50


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

    def update_all(self, data_init):
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


n, m = map(int, input().split())
l_dict = [[] for _ in range(n)]
r_dict = [[] for _ in range(n)]
edge = []
for i in range(m):
    l, r, c = map(int, input().split())
    l -= 1
    r -= 1
    l_dict[l].append(i)
    r_dict[r].append(i)
    edge.append((l, r, c))

dp = [INF] * n
dp[0] = 0
seg_rmq = SegTree(n, INF, min)
seg_rmq.update(0, 0)

for i in range(1, n):
    for j in r_dict[i]:
        l, r, c = edge[j]
        tmp = seg_rmq.query(l, r)
        dp[i] = min(dp[i], tmp + c)

    seg_rmq.update(i, dp[i])

ans = dp[-1] if dp[-1] != INF else -1

print(ans)
