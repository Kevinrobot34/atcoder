import sys
# input = sys.stdin.readline
input = sys.stdin.buffer.readline
import math
from itertools import combinations
EPS = 10**-7


class P2():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.norm2 = (self.x**2 + self.y**2)**0.5

    def __add__(self, other):
        return P2(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return P2(self.x - other.x, self.y - other.y)

    def __mul__(self, other: float):
        return P2(self.x * other, self.y * other)

    def __truediv__(self, other: float):
        return P2(self.x / other, self.y / other)

    def dot(self, other):
        return self.x * other.x + self.y * other.y

    def det(self, other):
        return self.x * other.y - self.y * other.x


class Circle():
    def __init__(self, p, r):
        self.p = p
        self.r = r


n, k = map(int, input().split())
p = []
c = []
for _ in range(n):
    x, y, cc = map(float, input().split())
    p.append(P2(x, y))
    c.append(cc)

dist = [[(p[i] - p[j]).norm2 for j in range(n)] for i in range(n)]


def check(r):
    circles = [Circle(p[i], r / c[i]) for i in range(n)]

    # 半径rの円２つの交点の列挙
    cand = [pi for pi in p]
    for c_i, c_j in combinations(circles, r=2):
        d_ij = c_i.p - c_j.p
        if d_ij.norm2 < c_i.r + c_j.r - EPS:
            # 点iと点jを中心とする円が交点を持つ時
            x = (c_j.r**2 - c_i.r**2 + d_ij.norm2**2) / (2 * d_ij.norm2)
            h = math.sqrt(max(c_j.r**2 - x**2, 0.0))
            v = P2(-d_ij.y, d_ij.x) * (h / d_ij.norm2)
            dx = c_j.p + d_ij * (x / d_ij.norm2)
            cand.append(dx + v)
            cand.append(dx - v)

    for cand_p in cand:
        cnt = 0
        for c_i in circles:
            if (c_i.p - cand_p).norm2 < c_i.r + EPS:
                cnt += 1
                if cnt >= k:
                    return True

    return False


lb = 0.0  # False
ub = 3000 * 100  # True
while ub - lb > EPS:
    mid = (ub + lb) / 2
    if check(mid):
        ub = mid
    else:
        lb = mid

print(ub)
