n = int(input())
k = int(input())
x = int(input())
y = int(input())

ans = x * min(k, n) + y * max(n - k, 0)

print(ans)
