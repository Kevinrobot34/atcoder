import sys
from operator import itemgetter
from bisect import bisect_left, bisect_right
input = sys.stdin.readline
MOD = 998244353


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


n = int(input())
robot = [tuple(map(int, input().split())) for _ in range(n)]
robot.sort(key=itemgetter(0))
x = [robot[i][0] for i in range(n)]

# dp[i] = (i番目のロボットを起動すると最終的にdp[i]番目まで起動する)
dp = [0] * n
dp[n - 1] = n - 1

st_rmq = SegmentTree1(n, 0, max)
st_rmq.update(n - 1, dp[n - 1])
for i in reversed(range(n - 1)):
    r = bisect_left(x, x[i] + robot[i][1])
    dp[i] = max(i, st_rmq.query(l=i + 1, r=r))
    st_rmq.update(i, dp[i])

# print(robot)
# print(dp)

# dp2[i] = (i番目以降のロボットのみで考えたときの場合の数)
dp2 = [0] * (n + 1)
dp2[n] = 1
for i in reversed(range(n)):
    # i番目を起動しない -> {i} + {i+1以降を起動した場合のパターン} : dp2[i+1]通り存在
    # i番目を起動する　 -> { } + {dp[i]+1以降を起動した場合のパターン} : dp2[dp[i]+1]通り存在
    dp2[i] = dp2[i + 1] + dp2[dp[i] + 1]
    dp2[i] %= MOD
# print(dp2)

print(dp2[0])
