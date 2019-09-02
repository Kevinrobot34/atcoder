m, d = map(int, input().split())

ans = 0
for mi in range(1, m+1):
    for di in range(1, d+1):
        if di % 10 >= 2 and di // 10 >= 2 and mi == (di // 10) * (di % 10):
            ans += 1

print(ans)
