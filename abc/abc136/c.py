n = int(input())
h = list(map(int, input().split()))

ans = True
m = 10**10
for i in reversed(range(n)):
    if h[i] <= m:
        m = h[i]
    elif h[i] > m+1:
        ans = False
        break

if ans:
    print("Yes")
else:
    print("No")
