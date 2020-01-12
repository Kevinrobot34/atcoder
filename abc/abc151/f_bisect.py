import math
EPS = 10**-8


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


n = int(input())
p = [P2(*map(int, input().split())) for _ in range(n)]

dist = [[(p[i] - p[j]).norm2 for j in range(n)] for i in range(n)]


def check(r):
    # 最小包含円の半径がr以下であるか

    # 半径rの円２つの交点の列挙
    cand = []
    for i in range(n - 1):
        for j in range(i + 1, n):
            c_ij = (p[i] + p[j]).smul(0.5)
            d_ij = p[i] - p[j]
            # cand.append(c_ij)

            if dist[i][j] < r * 2:
                # 点iと点jを中心とする半径rの円は交点を持つ時
                h = (r**2 - (dist[i][j] / 2)**2)**0.5
                v = P2(-d_ij.y, d_ij.x).smul(h / d_ij.norm2)
                cand.append(c_ij + v)
                cand.append(c_ij - v)

    for cand_p in cand:
        is_in = True
        for i in range(n):
            if (p[i] - cand_p).norm2 > r + EPS:
                is_in = False
                break
        if is_in:
            # print(r, cand_p.x, cand_p.y)
            return True
    return False
    # return any(all((pi - ci).norm2 <= r + EPS for pi in p) for ci in cand)


lb = 0.0  # False
ub = 2000  # True
while ub - lb > EPS:
    mid = (ub + lb) / 2
    if check(mid):
        ub = mid
    else:
        lb = mid

print(ub)
