h, w = map(int, input().split())
s = [input() for _ in range(h)]

ans = 0
for i in range(h):
    for j in range(w - 1):
        if s[i][j] == '.' and s[i][j + 1] == '.':
            ans += 1

for i in range(h - 1):
    for j in range(w):
        if s[i][j] == '.' and s[i + 1][j] == '.':
            ans += 1

print(ans)
