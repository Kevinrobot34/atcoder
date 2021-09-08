n, a, b = map(int, input().split())
ans = (n // (a + b)) * a + min((n % (a + b)), a)
print(ans)
