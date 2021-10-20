from bisect import bisect_left

n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

b.sort()

ans = 10**10
for ai in a:
    j = bisect_left(b, ai)
    if j > 0:
        ans = min(ans, abs(ai - b[j - 1]))
    if j < m:
        ans = min(ans, abs(ai - b[j]))

print(ans)
