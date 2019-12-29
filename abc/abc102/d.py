n = int(input())
a = list(map(int, input().split()))
a_cs = [0] * (n + 1)
for i in range(n):
    a_cs[i + 1] = a_cs[i] + a[i]

i1 = 1
i3 = 3
ans = 10**14
for i2 in range(2, n - 1):
    while i1 + 1 < i2 and abs(a_cs[i1] * 2 - a_cs[i2]) > abs(a_cs[i1 + 1] * 2 -
                                                             a_cs[i2]):
        i1 += 1

    while i3 + 1 < n and abs(a_cs[-1] + a_cs[i2] - a_cs[i3] *
                             2) > abs(a_cs[-1] + a_cs[i2] - a_cs[i3 + 1] * 2):
        i3 += 1

    p = a_cs[i1]  # [0,i1)
    q = a_cs[i2] - a_cs[i1]  # [i1, i2)
    r = a_cs[i3] - a_cs[i2]  # [i2, i3)
    s = a_cs[n] - a_cs[i3]  # [i3, n)
    cand = max(p, q, r, s) - min(p, q, r, s)
    ans = min(ans, cand)

print(ans)
