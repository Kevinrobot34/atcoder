n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

v = sum(a[i] * b[i] for i in range(n))
ans = 'Yes' if v == 0 else 'No'
print(ans)
