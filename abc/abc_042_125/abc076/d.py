n = int(input())
t = list(map(int, input().split()))
v = list(map(int, input().split()))

tc = 0
lrv = [(0, 0, 0)]
for ti, vi in zip(t, v):
    lrv.append((tc, tc + ti, vi))
    tc += ti
lrv.append((tc, tc, 0))


def func(x, l, r, v):
    if x <= l:
        return v + (l - x)
    elif x <= r:
        return v
    else:
        return v + (x - r)


ans = 0.0
v_prev = 0.0
for ti in range(1, 2 * tc + 1):
    ti /= 2.0
    vi = min(func(ti, li, ri, vi) for li, ri, vi in lrv)

    ans += (vi + v_prev) * 0.5 / 2.0
    v_prev = vi

print(ans)
