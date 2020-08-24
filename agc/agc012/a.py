n = int(input())
a = list(map(int, input().split()))

a.sort(reverse=True)
ans = sum(a[1:2 * n:2])
print(ans)
