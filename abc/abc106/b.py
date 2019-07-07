n = int(input())

ans = 0
for i in range(1, n+1):
    if i % 2 == 0:
        continue
    m = 0
    for j in range(1, i+1):
        if i % j == 0:
            m += 1

    if m == 8:
        ans += 1

print(ans)
