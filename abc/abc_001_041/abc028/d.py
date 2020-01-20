n, k = map(int, input().split())

cand = 1 + (n - k) * 3 + (k - 1) * 3 + (n - k) * (k - 1) * 6
ans = cand / (n**3)

print(ans)
