s = input()
n = len(s)
is_possible = True
for i in range(n // 2):
    if s[i] == '*' or s[n - 1 - i] == '*':
        continue
    if s[i] != s[n - 1 - i]:
        is_possible = False
        break

ans = 'YES' if is_possible else 'NO'
print(ans)
