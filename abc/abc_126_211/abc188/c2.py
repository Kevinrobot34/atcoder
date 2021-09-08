n = int(input())
a = list(map(int, input().split()))

x1 = max(a[:len(a) // 2])
x2 = max(a[len(a) // 2:])
ans = a.index(min(x1, x2)) + 1
print(ans)
