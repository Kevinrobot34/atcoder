n, a, b = map(int, input().split())
ans = 'Ant' if 0 < n % (a + b) <= a else 'Bug'
print(ans)
