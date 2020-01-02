r, c, k = map(int, input().split())
s = [input() for _ in range(r)]

cnt = [[0] * c for _ in range(r)]
for i in range(r):
    for j in range(c):
        if s[i][j] == 'x':
            cnt[i][j] = k

for i in range(r):
    # right
    for j in range(c - 1):
        cnt[i][j + 1] = max(cnt[i][j + 1], cnt[i][j] - 1)
    # left
    for j in reversed(range(1, c)):
        cnt[i][j - 1] = max(cnt[i][j - 1], cnt[i][j] - 1)

for j in range(c):
    # down
    for i in range(r - 1):
        cnt[i + 1][j] = max(cnt[i + 1][j], cnt[i][j] - 1)
    # up
    for i in reversed(range(1, r)):
        cnt[i - 1][j] = max(cnt[i - 1][j], cnt[i][j] - 1)

ans = 0
for i in range(k - 1, r - k + 1):
    for j in range(k - 1, c - k + 1):
        if cnt[i][j] == 0:
            ans += 1

# print(*cnt, sep='\n')
print(ans)
