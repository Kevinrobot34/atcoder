import sys
from heapq import heappop, heappush
from operator import itemgetter

input = sys.stdin.readline

n, m, q = map(int, input().split())
wv = [list(map(int, input().split())) for _ in range(n)]
wv.sort(key=itemgetter(0))
x = list(map(int, input().split()))

for _ in range(q):
    l, r = map(int, input().split())
    l -= 1
    y = x[:l] + x[r:]
    y.sort()
    ans = 0
    i = 0
    queue = []
    for yj in y:
        while i < n and wv[i][0] <= yj:
            heappush(queue, -wv[i][1])
            i += 1
        if len(queue) > 0:
            ans += -heappop(queue)
    print(ans)
