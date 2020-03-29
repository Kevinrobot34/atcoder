n = int(input())
c = [int(input()) for _ in range(n)]

div = [0] * n
for i in range(n):
    for j in range(n):
        if i == j:
            continue
        if c[i] % c[j] == 0:
            div[i] += 1

ans = 0
for i in range(n):
    if div[i] % 2 == 0:
        ans += (div[i] + 2) / (2 * div[i] + 2)
    else:
        ans += 0.5
print(ans)
