EPS = 1e-7


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


class Line():
    def __init__(self, v_dir: P2, b: P2):
        self.v_dir = v_dir  # 方向ベクトル
        self.b = b  # 切片的なベクトル

    def crosspoint(self, other):
        b = other.b - self.b
        c = self.v_dir.det(other.v_dir)
        if sgn(c) == 0:
            # 2つの直線が平行だったら以下を返す
            return False, None
        a = -other.v_dir.rot90().dot(b) / c
        return True, self.v_dir * a + self.b


px, py = map(int, input().split())
n = int(input())
fig_point = [tuple(map(int, input().split())) for _ in range(n)]

ans = float('inf')
p0 = P2(px, py)
for i in range(n + 1):
    p1 = P2(*fig_point[i % n])
    p2 = P2(*fig_point[(i + 1) % n])

    d1 = (p1 - p0).norm
    d2 = (p2 - p0).norm

    v_dir = p2 - p1
    l12 = Line(v_dir, p1)
    l0 = Line(v_dir.rot90(), p0)
    is_crossing, p_cross = l12.crosspoint(l0)
    if not is_crossing:
        continue

    d0 = (p_cross - p0).norm
    if d0 < d1 and d0 < d2:
        ans = min(ans, d0)

print(ans)
