n, r = map(int, input().split())
s = list(input())

ans = 0
for i in range(n - r + 1):
    not_yet = any(s[j] == '.' for j in range(i, i + r))
    if not_yet:
        if s[i] == '.':
            for j in range(i, i + r):
                s[j] = 'o'
            ans += 1
        elif i < n - r and all(s[j] == 'o' for j in range(i + r, n)):
            for j in range(i, i + r):
                s[j] = 'o'
            ans += 1

    if all(s[j] == 'o' for j in range(n)):
        break

    ans += 1

print(ans)
