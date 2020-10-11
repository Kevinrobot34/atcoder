MOD = 10**9 + 7
h, w = map(int, input().split())
s = ['#' * (w + 1)] + ['#' + input() + '#' for _ in range(h)] + ['#' * (w + 1)]

l = [[0] * (w + 2) for _ in range(h + 2)]
r = [[w + 1] * (w + 2) for _ in range(h + 2)]
for i in range(1, h + 1):
    for j in range(1, w + 1):
        l[i][j] = j if s[i][j] == '#' else l[i][j - 1]
    for j in reversed(range(1, w + 1)):
        r[i][j] = j if s[i][j] == '#' else r[i][j + 1]

u = [[0] * (w + 2) for _ in range(h + 2)]
d = [[h + 1] * (w + 2) for _ in range(h + 2)]
for j in range(1, w + 1):
    for i in range(1, h + 1):
        u[i][j] = i if s[i][j] == '#' else u[i - 1][j]
    for i in reversed(range(1, h + 1)):
        d[i][j] = i if s[i][j] == '#' else d[i + 1][j]

k = sum(s[i].count('.') for i in range(1, h + 1))

p = [1] * (k + 1)
for i in range(1, k + 1):
    p[i] = (p[i - 1] * 2) % MOD

ans = 0
for i in range(1, h + 1):
    for j in range(1, w + 1):
        if s[i][j] == '.':
            c = (r[i][j] - l[i][j] - 1) + (d[i][j] - u[i][j] - 1) - 1
            ans += (p[c] - 1) * p[k - c] % MOD
            ans %= MOD

print(ans)
