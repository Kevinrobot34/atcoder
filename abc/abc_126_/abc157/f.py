import sys
# input = sys.stdin.readline
input = sys.stdin.buffer.readline
import math
from itertools import combinations
EPS = 10**-7


class P2():
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y
        self.norm = (self.x**2 + self.y**2)**0.5

    def __add__(self, other):
        return P2(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return P2(self.x - other.x, self.y - other.y)

    def __mul__(self, c: float):
        return P2(self.x * c, self.y * c)

    def __truediv__(self, c: float):
        return P2(self.x / c, self.y / c)

    def __eq__(self, other):
        return (abs(self.x - other.x) < EPS) and (abs(self.y - other.y) < EPS)

    def dot(self, other) -> float:
        return self.x * other.x + self.y * other.y

    def det(self, other) -> float:
        return self.x * other.y - self.y * other.x

    def rot90(self):
        return P2(-self.y, self.x)


class Circle():
    def __init__(self, p: P2, r: float):
        self.p = p  # center of the circle
        self.r = r  # radius of the circle

    def contains(self, p: P2, allow_on_edge: bool) -> bool:
        if allow_on_edge:
            return (self.p - p).norm < self.r + EPS
        else:
            return (self.p - p).norm < self.r - EPS

    def cct(self, other) -> int:
        # count common tangent / 共通接線の数
        if self.p == other.p:
            # center is same
            if abs(self.r - other.r) < EPS:
                return float('inf')  # same
            else:
                return 0  # 内包

        d = other.p - self.p
        if d.norm > self.r + other.r + EPS:
            return 4  # 離れてる
        elif d.norm > self.r + other.r - EPS:
            return 3  # 外接
        elif d.norm > abs(self.r - other.r) + EPS:
            return 2  # 交点2つ
        elif d.norm > abs(self.r - other.r) - EPS:
            return 1  # 内接
        else:
            return 0  # 内包

    def intersection_points_with_circle(self, other) -> list:
        cct = self.cct(other)
        d = other.p - self.p

        if cct == 1:
            # 内接
            if self.r > other.r:
                return [self.p + d * (self.r / d.norm)]
            else:
                return [self.p - d * (self.r / d.norm)]
        elif cct == 3:
            # 外接
            return [self.p + d * (self.r / d.norm)]
        elif cct == 2:
            # 交点2個
            x = (self.r**2 - other.r**2 + d.norm**2) / (2 * d.norm)
            h = math.sqrt(max(self.r**2 - x**2, 0.0))
            v = d.rot90() * (h / d.norm)
            dx = self.p + d * (x / d.norm)
            return [dx + v, dx - v]

        return []


n, k = map(int, input().split())
p = []
c = []
for _ in range(n):
    x, y, cc = map(float, input().split())
    p.append(P2(x, y))
    c.append(cc)


def check(r):
    circles = [Circle(p[i], r / c[i]) for i in range(n)]

    # 半径rの円２つの交点の列挙
    cand = [pi for pi in p]
    for c_i, c_j in combinations(circles, r=2):
        cand_ij = c_i.intersection_points_with_circle(c_j)
        cand.extend(cand_ij)

    for cand_p in cand:
        cnt = 0
        for c_i in circles:
            if c_i.contains(cand_p, allow_on_edge=False)
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
