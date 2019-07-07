s = input()
k = int(input())

ans = s[0]
for i in range(min(k, len(s))):
    if s[i] != '1':
        ans = s[i]
        break

print(ans)
