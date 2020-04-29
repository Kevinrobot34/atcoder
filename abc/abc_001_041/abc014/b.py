n, x = map(int, input().split())
a = list(map(int, input().split()))

ans = sum(a[i] for i in range(n) if x & (1 << i))
print(ans)
