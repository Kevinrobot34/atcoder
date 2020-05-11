from operator import itemgetter
import sys
input = sys.stdin.readline
n = int(input())

magic1 = []
magic2 = []
magic3 = []
for _ in range(n):
    a, b = map(int, input().split())
    if a - b < 0:
        magic1.append((a, b))
    elif a - b == 0:
        magic2.append((a, b))
    else:
        magic3.append((a, b))

magic1.sort(key=itemgetter(0))
magic3.sort(key=itemgetter(1), reverse=True)
magic = magic1 + magic2 + magic3

ans = t = 0
for a, b in magic:
    ans = max(t + a, ans)
    t += a - b

print(ans)
