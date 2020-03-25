from operator import itemgetter
from bisect import bisect_right
import sys
input = sys.stdin.readline

n, d, a = map(int, input().split())
monster = [tuple(map(int, input().split())) for _ in range(n)]
monster.sort(key=itemgetter(0))
xx = [xi for xi, hi in monster]

ans = 0
imos = [0] * (n + 1)
for i, (xi, hi) in enumerate(monster):
    hi -= imos[i]
    if hi > 0:
        c = (hi + a - 1) // a
        ans += c
        idx = bisect_right(xx, xi + 2 * d)
        imos[i] += c * a
        imos[idx] -= c * a

    # update imos
    imos[i + 1] += imos[i]

print(ans)
