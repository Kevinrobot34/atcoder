import sys
input = sys.stdin.readline
EPS = 1e-7


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


n = int(input())
a = [P2(*map(int, input().split())) for _ in range(n)]
b = [P2(*map(int, input().split())) for _ in range(n)]


def get_farthest(p):
    p_center = P2(0, 0)
    for pi in p:
        p_center += pi
    p_center /= len(p)

    ans = P2(0, 0)
    for pi in p:
        di = pi - p_center
        if di.norm > ans.norm:
            ans = di
    return ans.norm


ans = get_farthest(b) / get_farthest(a)
print(ans)
