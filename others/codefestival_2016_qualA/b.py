n = int(input())
a = list(map(lambda x: int(x) - 1, input().split()))
ans = 0
for i in range(n):
    if a[a[i]] == i:
        ans += 1
ans //= 2
print(ans)
