s = input().lower()
t = 'ict'
j = 0

for i in range(len(s)):
    if s[i] == t[j]:
        j += 1
    if j == 3:
        break

ans = 'YES' if j == 3 else 'NO'
print(ans)
