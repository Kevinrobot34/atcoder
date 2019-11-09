s = input()

t = ''
for i in range(len(s)):
    if s[i] != 'B':
        t += s[i]
    elif len(t) >= 1:
        t = t[:-1]

print(t)
