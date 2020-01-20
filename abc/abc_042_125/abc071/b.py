from string import ascii_lowercase
s = input()

d = set([s[i] for i in range(len(s))])
ans = "None"
for c in ascii_lowercase:
    if c not in d:
        ans = c
        break

print(ans)
