n = int(input())

s0 = 2
t0 = a0 = 1
for i in range(n):
    t, a = map(int, input().split())

    m = max((t0 + t - 1) // t,
            (a0 + a - 1) // a)

    t0, a0 = t * m, a * m
    s0 = t0 + a0
    # print(s0, t0, a0, m)

print(s0)
