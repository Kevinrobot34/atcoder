n = int(input())
a = list(map(int, input().split()))

ans = sum(a[i + 1] - a[i] for i in range(n - 1)) / (n - 1)
print(ans)
