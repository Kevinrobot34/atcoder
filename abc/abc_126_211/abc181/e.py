from bisect import bisect_left
n, m = map(int, input().split())
h = list(map(int, input().split()))
w = list(map(int, input().split()))

h.sort()

h1 = [0] * n
for i in range(2, n, 2):
    h1[i] = h1[i - 2] + abs(h[i - 1] - h[i - 2])

h2 = [0] * n
for i in reversed(range(0, n - 2, 2)):
    h2[i] = h2[i + 2] + abs(h[i + 1] - h[i + 2])

ans = float('inf')
for wi in w:
    idx = bisect_left(h, wi)
    if idx % 2 == 1:
        idx -= 1
    ans = min(ans, h1[idx] + abs(wi - h[idx]) + h2[idx])

print(ans)
