from operator import itemgetter
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
xy = [tuple(map(int, input().split())) for _ in range(n)]
a = [int(input()) for _ in range(m)]

xy.sort(key=itemgetter(1, 0))
a.sort()
ans = 0
j = 0
for ai in a:
    while j < n:
        xj, yj = xy[j]
        if xj > ai:
            break
        elif yj < ai:
            j += 1
        else:
            ans += 1
            j += 1
            break

print(ans)
