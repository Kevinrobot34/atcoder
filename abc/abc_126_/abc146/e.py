from collections import defaultdict
from bisect import bisect_left, bisect_right
n, k = map(int, input().split())
a = list(map(int, input().split()))

a_cs = [0] * (n + 1)
for i in range(n):
    a_cs[i + 1] = a_cs[i] + a[i]

d = defaultdict(list)
for i in range(n + 1):
    d[(a_cs[i] - i) % k].append(i)

ans = 0
for l in range(n):
    idx_1 = bisect_right(d[(a_cs[l] - l) % k], l)
    idx_2 = bisect_left(d[(a_cs[l] - l) % k], l + k)
    ans += idx_2 - idx_1

print(ans)
