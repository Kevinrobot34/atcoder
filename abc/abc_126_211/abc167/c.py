n, m, x = map(int, input().split())
c = []
a = []
for _ in range(n):
    s = input().split()
    c.append(int(s[0]))
    a.append(list(map(int, s[1:])))

# print(c)
# print(*a, sep='\n')

ans = sum(c) + 1
for bit in range(1 << n):
    cand = 0
    b = [0] * m
    for i in range(n):
        if (bit >> i) & 1:
            cand += c[i]
            for j in range(m):
                b[j] += a[i][j]

    is_possible = True
    for j in range(m):
        if b[j] < x:
            is_possible = False
            break

    if is_possible:
        ans = min(ans, cand)

if ans == sum(c) + 1:
    print(-1)
else:
    print(ans)
