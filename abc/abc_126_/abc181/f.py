from collections import defaultdict
from itertools import product
EPS = 1e-10


def sgn(a: float):
    if a < -EPS:
        return -1
    elif a > EPS:
        return 1
    else:
        return 0


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


def is_crossing(p1, p2, q1, q2) -> bool:
    # 点p1と点p2を端点とする線分と、点q1と点q2を端点とする線分が交差するかを判定する関数
    if sgn((q2 - q1).det(p2 - p1)) == 0:
        # 誤差の範囲で平行
        return False
    ta = (q2 - q1).det(q1 - p1) / (q2 - q1).det(p2 - p1)
    tb = (p2 - p1).det(p1 - q1) / (p2 - p1).det(q2 - q1)
    return (0.0 <= ta <= 1.0) and (0.0 <= tb <= 1.0)


def func(x_prev, y_prev_list, x_lim, x_curr, y_curr_list):
    p_prev = [P2(x_prev, yi) for yi in y_prev_list]
    p_curr = [P2(x_curr, yi) for yi in y_curr_list]

    res = []
    for i in range(1, len(y_curr_list)):
        pi = P2(x_curr, (y_curr_list[i - 1] + y_curr_list[i]) / 2)
        z = 0
        for j in range(1, len(y_prev_list)):
            pj = P2(x_prev, (y_prev_list[j - 1] + y_prev_list[j]) / 2)
            zz = min(abs(y_curr_list[i - 1] - y_curr_list[i]),
                     abs(y_prev_list[j - 1] - y_prev_list[j]))
            for pa, pb in product(p_prev, p_curr):
                if is_crossing(pi, pj, pa, pb):
                    zz = min(zz, (pa - pb).norm)
                    # print(pa.x, pa.y, pb.x, pb.y, (pa - pb).norm, zz)
            z = max(z, zz)
        res.append(z)
    return res


n = int(input())
points = defaultdict(set)
points[-100] = set((-100, 100))
points[+100] = set((-100, 100))
for _ in range(n):
    x, y = map(int, input().split())
    points[x].add((y))
    points[x].add((-100))
    points[x].add((+100))

points = {k: sorted(v) for k, v in points.items()}
x_list = sorted(list(points.keys()))
print(x_list)
print(points)

res = [200]
for i in range(len(x_list) - 1):
    x0 = x_list[i + 0]
    x1 = x_list[i + 1]
    res = func(x0, points[x0], res, x1, points[x1])
    print(x1, res)
