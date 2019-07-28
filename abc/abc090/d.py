n, k = map(int, input().split())

ans = 0
for c in range(k, n+1):
    for b in range(c+1, n+1):
        # print(b, c, (n-c) // b + 1)
        if c != 0:
            ans += (n-c) // b + 1
        else:
            ans += (n-c) // b

print(ans)
