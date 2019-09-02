from collections import defaultdict
MOD = 10**9 + 7
n = int(input())

d = defaultdict(int)
for m in range(2, n+1):
    while m % 2 == 0:
        d[2] += 1
        m = m // 2

    p = 3
    while m > 1:
        while m % p == 0:
            d[p] += 1
            m = m // p
        p += 2

ans = 1
for k, v in d.items():
    ans *= v + 1
    ans %= MOD

print(ans)
