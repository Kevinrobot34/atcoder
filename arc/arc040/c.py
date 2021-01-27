n = int(input())
s = [list(input()) for _ in range(n)]

ans = 0
for i in range(n):
    for j in reversed(range(n)):
        if s[i][j] == '.':
            for k in range(j + 1):
                s[i][k] = 'o'
            if i < n - 1:
                for k in range(j, n):
                    s[i + 1][k] = 'o'
            ans += 1

print(ans)
