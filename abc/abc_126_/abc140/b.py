n  = int(input())

a = list(map(lambda x: int(x)-1, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))

ans = 0
for i in range(n):
    ans += b[i]
    if i > 0 and a[i] - a[i-1] == 1:
        ans += c[a[i-1]]

print(ans)
