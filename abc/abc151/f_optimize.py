import math
from scipy.optimize import fmin
# https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.fmin.html


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


def func(cp):
    cp = P2(*cp)
    return max((cp - pi).norm2 for pi in p)


res_cp = fmin(func, [500, 500], disp=False)
ans = func(res_cp)
print(ans)
