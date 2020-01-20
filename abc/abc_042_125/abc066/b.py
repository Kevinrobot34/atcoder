s = input()

for i in reversed(range(1, len(s)//2)):
    if s[:i] == s[i:2*i]:
        ans = i * 2
        break

print(ans)
