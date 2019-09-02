s = input()

ans = ''
d = {'1': '9', '9': '1'}
for i in range(len(s)):
    ans += d[s[i]]

print(ans)
