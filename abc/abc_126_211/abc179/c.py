n = int(input())
ans = sum((n - 1) // a for a in range(1, n))
print(ans)
