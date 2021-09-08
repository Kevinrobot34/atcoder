n = int(input())
a = list(map(int, input().split()))

s = sum(ai**2 for ai in a)
t = sum(a)**2
ans = s * n - t
print(ans)
