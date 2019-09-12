s = input()

np = 0
for i in range(len(s)):
    if s[i] == 'p':
        np += 1

ans = len(s) // 2 - np
print(ans)
