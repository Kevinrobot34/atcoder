n, l = map(int, input().split())

amida = list(range(1, n + 1))
for _ in range(l):
    s = input()
    for i in range(n - 1):
        if s[i * 2 + 1] == '-':
            amida[i], amida[i + 1] = amida[i + 1], amida[i]

y = input()
for i in range(n):
    if y[i * 2] == 'o':
        ans = amida[i]
print(ans)
