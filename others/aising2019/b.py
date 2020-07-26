from bisect import bisect_right
n = int(input())
a, b = map(int, input().split())
p = list(map(int, input().split()))
p.sort()

idx_a = bisect_right(p, a)
idx_b = bisect_right(p, b)

ans = min(idx_a, idx_b - idx_a, n - idx_b)
print(ans)
