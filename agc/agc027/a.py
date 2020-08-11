from bisect import bisect_left
n, x = map(int, input().split())
a = list(map(int, input().split()))
a.sort()

a_cs = [0] * (n + 1)
for i in range(n):
    a_cs[i + 1] = a_cs[i] + a[i]

idx = bisect_left(a_cs, x)
if idx == n + 1:
    ans = n - 1
elif a_cs[idx] > x:
    ans = idx - 1
else:
    ans = idx
print(ans)
