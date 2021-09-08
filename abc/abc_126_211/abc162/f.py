import sys
sys.setrecursionlimit(10**8)

n = int(input())
a = list(map(int, input().split()))

a_cs = [0] * (n + 1)
a_cs[-2] = a[-1]
for i in reversed(range(n - 1)):
    a_cs[i] = a[i] + a_cs[i + 2]
# print(a_cs)

d = {}


def func(i):
    if i == n:
        return 0
    if i == n - 1:
        return a[-1]
    if i in d:
        return d[i]

    m = n - i
    if m % 2 == 0:
        ans0 = a[i] + func(i + 2)
        ans1 = a_cs[i + 1]
        ans = max(ans0, ans1)
    else:
        ans0 = a[i + 0] + func(i + 2)
        ans1 = a[i + 1] + func(i + 3)
        ans2 = a_cs[i + 2]
        ans = max(ans0, ans1, ans2)

    d[i] = ans
    return ans


ans = func(0)

print(ans)
