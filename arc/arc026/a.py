n, a, b = map(int, input().split())
ans = n * a - (a - b) * min(n, 5)
print(ans)
