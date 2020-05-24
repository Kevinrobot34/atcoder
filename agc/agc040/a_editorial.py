s = input()

a1 = [0] * (len(s) + 1)
for i in range(len(s)):
    if s[i] == '<':
        a1[i + 1] = a1[i] + 1
a2 = [0] * (len(s) + 1)
for i in reversed(range(len(s))):
    if s[i] == '>':
        a2[i] = a2[i + 1] + 1

ans = 0
for i in range(len(a1)):
    ans += max(a1[i], a2[i])
print(ans)
