from bisect import bisect_left, bisect_right

n, m, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
a_cs = [0] * (n + 1)
b_cs = [0] * (m + 1)

for i in range(n):
    a_cs[i + 1] = a_cs[i] + a[i]
for i in range(m):
    b_cs[i + 1] = b_cs[i] + b[i]

ans = 0
for i in range(n + 1):
    if a_cs[i] <= k:
        cand = i
        cand += bisect_right(b_cs, k - a_cs[i]) - 1
        ans = max(ans, cand)

print(ans)
