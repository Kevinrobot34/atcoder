s = input()

a1 = a2 = 0
for i in range(len(s)):
    if i % 2 == 0:
        if s[i] == '0':
            a2 += 1
        else:
            a1 += 1
    else:
        if s[i] == '0':
            a1 += 1
        else:
            a2 += 1

print(min(a1, a2))
