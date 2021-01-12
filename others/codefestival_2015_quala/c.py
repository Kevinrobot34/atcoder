import sys
input = sys.stdin.readline

n, t = map(int, input().split())
ab = [list(map(int, input().split())) for _ in range(n)]
ab.sort(key=lambda x: x[1] - x[0])

s = sum(ai for ai, _ in ab) - t
ans = 0
for ai, bi in ab:
    if s <= 0:
        break
    s -= ai - bi
    ans += 1

if ans == n and s > 0:
    ans = -1

print(ans)
