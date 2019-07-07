s = input()

ans = 0
c = '?'
x = 0
for i in range(len(s)):
    if c == '?':
        c = s[i]
        x = 1
    elif c != s[i]:
        x -= 1
        ans += 2
        if x == 0:
            c = '?'
    else:
        x += 1

print(ans)
