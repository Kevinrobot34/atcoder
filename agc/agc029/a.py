s = input()

n_b = 0
for i in range(len(s)):
    if s[i] == 'B':
        n_b += 1

ans = 0
j = 0
for i in range(len(s)):
    if s[i] == 'B':
        j += 1
        ans += (len(s) - j) - i

print(ans)
