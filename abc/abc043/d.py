s = input()

ans = [-1, -1]
for i in range(1, len(s)):
    if s[i-1] == s[i]:
        ans = [i, i+1]
        break
    elif i >= 2 and s[i-2] == s[i]:
        ans = [i-1, i+1]

print(*ans)
