n, k = map(int, input().split())
s = [int(input()) for _ in range(n)]

ans = 0
s_prod = s[0]
r = 1
for l in range(n):
    if s[l] == 0:
        ans = n
        break

    while r < n and s_prod * s[r] <= k:
        s_prod *= s[r]
        r += 1
    # print(l, r, s_prod)

    if r - l == 0:
        r += 1
    elif r - l >= 1 and s_prod <= k:
        ans = max(ans, r-l)
        s_prod //= s[l]

print(ans)
