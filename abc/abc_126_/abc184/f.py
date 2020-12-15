from bisect import bisect_left, bisect_right

n, t = map(int, input().split())
a = list(map(int, input().split()))
nh = n // 2

a1 = []
a2 = []
for bit in range(1 << nh):
    s = sum(a[i] for i in range(nh) if (bit >> i) & 1)
    a1.append(s)

for bit in range(1 << (n - nh)):
    s = sum(a[nh + i] for i in range(n - nh) if (bit >> i) & 1)
    a2.append(s)

a2.sort()
ans = 0
for a1i in a1:
    idx = bisect_right(a2, t - a1i) - 1
    if idx >= 0:
        ans = max(ans, a1i + a2[idx])

print(ans)
