x1, y1, r = map(int, input().split())
x2, y2, x3, y3 = map(int, input().split())


def dist(ax, ay, bx, by):
    return ((ax - bx)**2 + (ay - by)**2)**0.5


ans_r = not ((x2 <= x1 - r) and (x1 + r <= x3) and (y2 <= y1 - r) and
             (y1 + r <= y3))
ans_b = not ((dist(x1, y1, x2, y2) <= r) and (dist(x1, y1, x2, y3) <= r) and
             (dist(x1, y1, x3, y2) <= r) and (dist(x1, y1, x3, y3) <= r))

ans_r = 'YES' if ans_r else 'NO'
ans_b = 'YES' if ans_b else 'NO'
print(ans_r)
print(ans_b)
