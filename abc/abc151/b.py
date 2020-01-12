n, k, m = map(int, input().split())
a = list(map(int, input().split()))

cand = m * n - sum(a)
ans = max(0, cand) if cand <= k else -1
print(ans)
