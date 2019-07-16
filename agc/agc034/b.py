s = input()
s = s.replace("BC", 'D')

ans = 0
x = 0
for i in range(len(s)):
    if s[i] == 'A':
        x += 1
    elif s[i] == 'D':
        ans += x
    else:
        x = 0

print(ans)
