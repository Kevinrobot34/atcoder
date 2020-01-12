import math
EPS = 1e-10


class P2():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.norm2 = (self.x**2 + self.y**2)**0.5

    def __add__(self, other):
        return P2(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return P2(self.x - other.x, self.y - other.y)

    def smul(self, a):
        return P2(self.x * a, self.y * a)

    def dot(self, other):
        return self.x * other.x + self.y * other.y

    def det(self, other):
        return self.x * other.y - self.y * other.x

    def rot90(self):
        return P2(-self.y, self.x)


def sgn(a: float):
    if a < -EPS:
        return -1
    elif a > EPS:
        return 1
    else:
        return 0


def simple_ccw(a, b, c):
    # Simple Counterclockwise test
    return sgn((b - a).det(c - a))


class Line():
    def __init__(self, dir: P2, b: P2):
        self.dir = dir
        self.b = b

    def crosspoint(self, other):
        b = other.b - self.b
        c = self.dir.det(other.dir)
        if sgn(c) == 0:
            # 2つの直線が平行だったら以下を返す
            return False, None
        a = -other.dir.rot90().dot(b) / c
        return True, self.dir.smul(a) + self.b


def gaisin(p1, p2, p3):
    l1 = Line((p2 - p1).rot90(), (p2 + p1).smul(0.5))
    l2 = Line((p3 - p1).rot90(), (p3 + p1).smul(0.5))
    return l1.crosspoint(l2)  # (bool, P2)


# l1 = Line(P2(2, 1), P2(0, 0))
# l2 = Line(P2(1, 1), P2(0, 1))
# is_exist, cp = l1.crosspoint(l2)
# print(is_exist, (cp.x, cp.y) if is_exist else "None")
# is_exist, cp = l2.crosspoint(l1)
# print(is_exist, (cp.x, cp.y) if is_exist else "None")

n = int(input())
p = [P2(*map(int, input().split())) for _ in range(n)]

cand = []
for i in range(n):
    for j in range(i + 1, n):
        # 中点
        cand.append((p[i] + p[j]).smul(0.5))
        for k in range(j + 1, n):
            # 3点の外心
            is_exist, cp = gaisin(p[i], p[j], p[k])
            if is_exist:
                cand.append(cp)

ans = 1000
for cp in cand:
    r_cand = max((pi - cp).norm2 for pi in p)
    ans = min(r_cand, ans)

print(ans)
