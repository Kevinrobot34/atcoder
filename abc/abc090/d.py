n, k = map(int, input().split())

ans = 0
if k == 0:
    ans = n * n
else:
    for b in range(k+1, n+1):
        ans += (n // b) * (b-k)
        ans += max(((n % b) - k + 1), 0)
        # print(b, (n // b) * (b-k) + max(((n % b) - k + 1), 0))

print(ans)
