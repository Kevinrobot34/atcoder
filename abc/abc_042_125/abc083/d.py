s = input()

t = []
x = s[0]
y = 0
for i in range(len(s)):
    if s[i] == x:
        y += 1
    else:
        t.append(y)
        y = 0
        x = s[i]

print(t)
ans = max(t)


print(ans)
