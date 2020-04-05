from math import gcd
n, q = map(int, input().split())
a = list(map(int, input().split()))
s = list(map(int, input().split()))

a_gcd = [a[0]]
for i in range(1, n):
    a_gcd.append(gcd(a_gcd[-1], a[i]))
# print(a_gcd)


def func(x):
    def check(i):
        if i == -1:
            return False
        return gcd(x, a_gcd[i]) == 1

    lb = -1  # False
    ub = n - 1  # True
    while ub - lb > 1:
        mid = (ub + lb) // 2
        if check(mid):
            ub = mid
        else:
            lb = mid
    return ub + 1


for i in range(q):
    cand = gcd(a_gcd[-1], s[i])
    if cand > 1:
        ans = cand
    else:
        ans = func(s[i])
    print(ans)
