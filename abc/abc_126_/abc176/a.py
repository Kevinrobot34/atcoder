n, x, t = map(int, input().split())
ans = ((n + x - 1) // x) * t
print(ans)
