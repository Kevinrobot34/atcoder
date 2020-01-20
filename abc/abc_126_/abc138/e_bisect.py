from collections import defaultdict
from bisect import bisect_left, bisect_right
s = input()
t = input()

n = len(s)
ds = defaultdict(list)
for i in range(n*2):
    ds[s[i%n]].append(i)

ans = 0
x = -1
for i in range(len(t)):
    if t[i] not in ds:
        ans = -1
        break

    x_next = ds[t[i]][bisect_right(ds[t[i]], x)]
    ans += x_next - x
    x = x_next % n
    # print(ans, t[i])

print(ans)
