from math import gcd
n, q = map(int, input().split())
a = list(map(int, input().split()))
s = list(map(int, input().split()))

a_gcd = [a[0]]
for i in range(1, n):
    a_gcd.append(gcd(a_gcd[-1], a[i]))
# print(a_gcd)

for i in range(q):
    cand = gcd(a_gcd[-1], s[i])
    if cand > 1:
        ans = cand
    else:
        lb = -1  # False
        ub = n - 1  # True
        while ub - lb > 1:
            mid = (ub + lb) // 2
            if gcd(s[i], a_gcd[mid]) == 1:
                ub = mid
            else:
                lb = mid
        ans = ub + 1
    print(ans)
