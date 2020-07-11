import sys
from operator import itemgetter
from heapq import heappush, heappop
input = sys.stdin.readline


def simulate(camels):
    camels.sort(key=itemgetter(0))
    queue = []
    ans = 0
    for k, l, r in camels:
        ans += l
        if len(queue) < k:
            # ok
            heappush(queue, l - r)
        else:
            heappush(queue, l - r)
            d = heappop(queue)
            ans -= d
    return ans


def solve():
    n = int(input())
    camels = [tuple(map(int, input().split())) for _ in range(n)]

    ans = 0
    camels_l = []
    camels_r = []
    for k, l, r in camels:
        if k == n or l == r:
            ans += l
        elif l > r:
            camels_l.append((k, l, r))
        else:
            # r > l
            camels_r.append((n - k, r, l))

    ans += simulate(camels_l)
    ans += simulate(camels_r)

    print(ans)


t = int(input())
for _ in range(t):
    solve()
