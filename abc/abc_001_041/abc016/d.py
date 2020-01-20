class P2():
    def __init__(self, x, y):
        self.x = x
        self.y = y

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


def on_seg(p1, p2, q) -> bool:
    is_online = (p1 - q).det(p2 - q) == 0
    is_between = (p1 - q).dot(p2 - q) <= 0
    return is_online and is_between


def is_crossing(p1, p2, q1, q2) -> bool:
    ta = (q2 - q1).det(q1 - p1) / (q2 - q1).det(p2 - p1)
    tb = (p2 - p1).det(p1 - q1) / (p2 - p1).det(q2 - q1)
    return (0.0 <= ta <= 1.0) and (0.0 <= tb <= 1.0)


def intersection(p1, p2, q1, q2):
    t = (q2 - q1).det(q1 - p1) / (q2 - q1).det(p2 - p1)
    return p1 + (p2 - p1).smul(t)


xa, ya, xb, yb = map(int, input().split())
pa = P2(xa, ya)
pb = P2(xb, yb)
n = int(input())
p_list = [P2(*map(int, input().split())) for _ in range(n)]
cnt = 0
for i in range(n):
    if (pb - pa).det(p_list[i] - p_list[i - 1]) != 0.0:
        # 平行でない
        if is_crossing(pa, pb, p_list[i - 1], p_list[i]):
            cnt += 1

ans = 1 + cnt // 2
print(ans)
