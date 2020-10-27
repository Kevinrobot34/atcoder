from itertools import permutations
from operator import itemgetter
from bisect import bisect_left, bisect_right
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
w = list(map(int, input().split()))
lv = [list(map(int, input().split())) for _ in range(m)]
lv.sort(key=itemgetter(1))
v = [vi for _, vi in lv]
l_max = [0] * (m + 1)
for i in reversed(range(m)):
    l_max[i] = max(l_max[i + 1], lv[i][0])


def calc(wp):
    wp_cs = [0] * (n + 1)
    for i in range(n):
        wp_cs[i + 1] = wp_cs[i] + wp[i]

    x = [[0] * (n + 1) for _ in range(n + 1)]
    for i in range(n):
        for j in range(i + 1, n):
            idx = bisect_left(v, wp_cs[j] - wp_cs[i])
            x[i][j] = l_max[idx]

    dp = [0] * (n + 1)
    for i in range(n):
        dp[i + 1] = sum(dp[j] + x[i][j] for j in range(i + 1))


if max(w) > min(lv[0][1]):
    ans = -1
else:
    ans = 10**10
    for wp in permutations(w):
        ans = min(ans, calc(wp))

print(ans)
