s = input()
s += '_'

ans = ''
c = s[0]
cnt = 0
for i in range(len(s)):
    if c != s[i]:
        ans += c + str(cnt)
        c = s[i]
        cnt = 1
    else:
        cnt += 1

print(ans)
