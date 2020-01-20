n = int(input())
a = list(map(int, input().split()))

ans = 0
l = r = 0
while l < n:
    while r+1 < n and a[r] < a[r+1]:
        r += 1
    ans += (r-l+1)*(r-l)//2 + (r-l+1)

    l, r = r+1, r+1

print(ans)
