from collections import defaultdict
from bisect import bisect_left, bisect_right
n = int(input())
rh = []
r = []
hands = defaultdict(lambda: defaultdict(int))
for i in range(n):
    ri, hi = map(int, input().split())
    hi %= 3
    rh.append((ri, hi))
    r.append(ri)
    hands[ri][hi] += 1
r.sort()

for ri, hi in rh:
    w = bisect_left(r, ri) + hands[ri][(hi + 1) % 3]
    d = hands[ri][hi] - 1
    l = n - 1 - w - d
    print(w, l, d)
