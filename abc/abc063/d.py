import math
n, a, b = map(int, input().split())
h = [int(input()) for _ in range(n)]
h.sort(reverse=True)

def check(m):
    m2 = m
    for i in range(n):
        if h[i] <= b * m:
            continue
        m2 -= math.ceil((h[i] - b * m) / (a - b))
        if m2 < 0:
            return False
    return True

l, r = 0, sum(h)//b+1
while r - l > 1:
    mid = (r + l) // 2
    # print(l, r, mid, check(mid))
    if check(mid):
        r = mid
    else:
        l = mid

print(r)
