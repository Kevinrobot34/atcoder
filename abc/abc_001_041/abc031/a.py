a, d = map(int, input().split())
ans = max((a + 1) * d, a * (d + 1))
print(ans)
