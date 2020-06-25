import sys
input = sys.stdin.readline

r, c, d = map(int, input().split())
a = [tuple(map(int, input().split())) for _ in range(r)]

ans = 0
i0 = j0 = 0
for i in range(r):
    for j in range(c):
        dist = abs(i - i0) + abs(j - j0)
        if dist <= d and (d - dist) % 2 == 0:
            ans = max(ans, a[i][j])

print(ans)
