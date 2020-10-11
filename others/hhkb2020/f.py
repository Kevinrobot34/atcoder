def modinv(x: int, mod: int) -> int:
    return pow(x, mod - 2, mod)


MOD = 10**9 + 7
n = int(input())
lr = [list(map(int, input().split())) for _ in range(n)]

l_max = 0
seg = set()
for li, ri in lr:
    l_max = max(l_max, li)
    seg.add(li)
    seg.add(ri)
seg = sorted(list(seg))
m = [0] * len(seg)
d = [1] * len(seg)
for i in range(1, len(seg)):
    for li, ri in lr:
        if seg[i] <= li or ri <= seg[i - 1]:
            d[i] *= ri - li
            d[i] %= MOD
        else:
            m[i] += 1

print(seg)
print(m)
print(d)

x = 1
# for li, ri in lr:
#     x *= ri - li
#     x %= MOD
for i in range(1, n + 2):
    x *= i
    x %= MOD

print(x)
ans = 0
for i in range(1, len(seg)):
    if seg[i] <= l_max:
        continue

    c = (m[i] * seg[i] + seg[i - 1]) % MOD
    c *= pow(seg[i] - seg[i - 1], m[i], MOD)
    c %= MOD
    ans += x * d[i] * c * modinv(m[i] + 1, MOD) % MOD
    ans %= MOD
print(ans)
