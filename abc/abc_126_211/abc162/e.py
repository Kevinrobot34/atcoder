import sys
sys.setrecursionlimit(10**8)
MOD = 10**9 + 7

n, k = map(int, input().split())

d = {}


def func1(kk):
    # 1-kをn個並べる時、gcdが1となる通り数
    if kk == 1:
        return 1
    if kk in d:
        return d[kk]

    cnt = 0
    for x in range(2, kk + 1):
        y = kk // x
        cnt += func1(y)

    d[kk] = (MOD + pow(kk, n, MOD) - cnt) % MOD
    return d[kk]


ans2 = 0
cnt = 0
for x in range(2, k + 1):
    y = k // x
    if y > 1:
        cnt = func1(y)
        ans2 += cnt * x % MOD
        ans2 %= MOD
    else:
        ans2 += x
        ans2 %= MOD

ans1 = func1(k)
ans = ans1 + ans2
ans %= MOD
# print(ans1, ans2)
print(ans)
