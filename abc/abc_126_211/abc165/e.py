n, m = map(int, input().split())

ans = []
if m % 2 == 0:
    for i in range(1, m // 2 + 1):
        ans.append((i, m - i + 2))
        ans.append((m + i + 1, 2 * m - i + 2))
else:
    for i in range(1, m // 2 + 1):
        ans.append((i, m - i + 2))
        ans.append((m + i + 1, 2 * m - i + 2))
    ans.append(((m + 1) // 2, (m + 1) // 2 + 1))

for a, b in ans:
    print(a, b)
