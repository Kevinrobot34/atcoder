a, r, n = map(int, input().split())
TH = 10**9

if r == 1:
    ans = a
else:
    ans = a
    for i in range(1, n):
        ans *= r
        if ans > TH:
            ans = 'large'
            break

print(ans)
